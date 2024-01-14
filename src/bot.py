import os
import random

import openai
import requests

from src.resize_image import resize_image

key = os.getenv('OPENAI_API_KEY') # get this on their website

class AI():
    def __init__(self, api_key):
        openai.api_key=api_key

    def ask(self, prompt, model='text-davinci-003', temperature=0, max_tokens=600, top_p=1.0, frequency_penalty=0.5, presence_penalty=0.0):
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        return response['choices'][0]["text"]

    def draw(self, prompt, n, size = "1024x1024"):
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            n=n,
            size=size,
        )
        return response

    def recreate_image(self, image_path, n, size = "1024x1024"):
        image = self.resize_image_4mb(image_path)
        image.seek(0)
        image_binary = image.read()
        response = openai.Image.create_variation(image_binary, n=n, model="dall-e-3", size=size)
        return response

    @staticmethod
    def resize_image_4mb(image_path):
        return resize_image(image_path=image_path)

    @staticmethod
    def generate_id():
        return random.randint(1111,9999)

    @staticmethod
    def parse_urls(draw_payload):
        return [item["url"] for item in draw_payload["data"]]

    @staticmethod
    def make_dirs_if_not_exists(path: str):
        path_parts = path.split(os.path.sep)
        current_path = ""

        for part in path_parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                print(f"Could not find dir {current_path}, creating now")
                os.makedirs(current_path)

    def download(self, prompt, draw_payload, download_path=None):
        print("Downloading your nicely made drawings")
        if len(prompt) > 15:
            prompt = prompt[:15]
        urls = self.parse_urls(draw_payload)
        dir = download_path or '.'
        self.make_dirs_if_not_exists(dir)
        for url in urls:
            img_data = requests.get(url).content
            with open(f'{dir}/{prompt}_{self.generate_id()}.jpg', 'wb') as handler:
                handler.write(img_data)

def make_bot():
    print("CREATING BOT...")
    return AI(key)