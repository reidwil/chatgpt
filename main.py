import sys
import os
import argparse
import pathlib # for writing python functions into files
import openai # for making the python functions
import requests
import random

key = os.getenv('OPENAI_API_KEY') # get this on their website

def get_args():
    output = argparse.ArgumentParser(description="A python cli that allows you to ask and draw pictures upon giving openai's bots some topics.")
    output.add_argument('--ask', type=str, help="Text input of what you'd like to ask the bot")
    output.add_argument('--draw', type=str, help="Text input of what you'd like to see drawn")
    output.add_argument('-n', type=int, required=False, help="N times you want the bot to run - default is 2")
    output.add_argument('--download', action='store_true', help="Should download the file?")
    output.parse_args()
    if len(sys.argv)==1:
        output.print_help(sys.stderr)
        sys.exit(1)
    return output

class AI():
    def __init__(self, api_key):
        openai.api_key=api_key

    def ask(self, prompt, model='text-davinci-003', temperature=0, max_tokens=600, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        return response

    def draw(self, prompt, n = None, size = "1024x1024"):
        if not n:
            n = 2
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )

        return response

    def generate_id(self):
        return random.randint(1111,9999)

    def parse_urls(self, draw_payload):
        return [item["url"] for item in draw_payload["data"]]

    def download(self, prompt, draw_payload):
        print("Downloading your nicely made drawings")
        urls = self.parse_urls(draw_payload)
        for id, url in enumerate(urls):
            img_data = requests.get(url).content
            with open(f'{prompt}_{self.generate_id()}.jpg', 'wb') as handler:
                handler.write(img_data)

def run():
    bot = AI(key)
    arguments = get_args().parse_args()
    if arguments.ask:
        response = bot.ask(arguments.ask)
        print(response)
    if arguments.draw:
        image_location = bot.draw(arguments.draw, n=arguments.n)
        print(image_location)
    if arguments.download:
        bot.download(arguments.draw, image_location)

if __name__=='__main__':
    run()
