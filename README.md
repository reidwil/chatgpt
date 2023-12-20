# chatgpt
Interact with chatgpt!


## Getting started
0. To use this program you need to generate an [openai api key](https://beta.openai.com/account/api-keys). After generating your api key, the program will look specifically for it in the python environment under the specific env var `OPENAI_API_KEY`. 

1. Run `$ pipenv install --dev`
2. Run `$ pyenv shell`
3. Run the main.py file: `$ python main.py`


-----------------
## Usage:

```
usage: main.py [-h] [--ask ASK] [--draw DRAW] [-n N] [--download]

A python cli that allows you to ask and draw pictures upon giving openai's bots some topics.

options:
  -h, --help   show this help message and exit
  --ask ASK    Text input of what you'd like to ask the bot
  --draw DRAW  Text input of what you'd like to see drawn
  -n N         N times you want the bot to run - default is 2
  --download   Should download the file?
```
---------------

## Example

To draw five pictures with the prompt "cool figure in white" and download those drawn photos you can run:

`$ python main.py --draw "cool figure in white" -n 5 --download`

