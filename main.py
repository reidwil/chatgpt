import os
import argparse
import pathlib # for writing python functions into files
import openai # for making the python functions


key = "$CHATGPT_API_KEY" # get this on their website

def get_args():
    output = argparse.ArgumentParser(description="A CLI that will help you")
    output.add_argument('--ask', type=str, help="Text input of what you'd like to ask the bot")
    output.add_argument('--draw', type=str, help="Text input of what you'd like to see drawn")
    output.add_argument('--output-file', type=os.PathLike)
    output.parse_args()
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

    def draw(self, prompt, n = 2, size = "1024x1024"):
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )

        return response
        
def run():
    bot = AI(key)
    arguments = get_args().parse_args()
    if arguments.ask:
        response = bot.ask(arguments.ask)
        print(response)
    if arguments.draw:
        image_location = bot.draw(arguments.draw)
        print(image_location)

if __name__=='__main__':
    run()
