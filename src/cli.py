import click
from bot import make_bot

@click.group()
def cli():
    pass

@cli.command()
@click.option('--prompt', '-p', 
              help='String text you would like bot to draw')
@click.option('--number','-n', default=3, 
              help="The number of pictures to make")
@click.option('--size','-s', default="1024x1024", 
              help="The pixel size image to draw")
@click.option('--download', '-d', is_flag=True, show_default=True, default=False, 
              help="Should the photos be downloaded?")
@click.option('--path', default="./photos", help="The file path to download the drawings to")
def draw(prompt, number, size, download, path):
    bot_instance = make_bot()
    result = bot_instance.draw(prompt, number, size)
    if download:
        bot_instance.download(prompt, result, path)
    click.echo(result)

@cli.command()
@click.option('--prompt', '-p',
              help='The prompt given to the bot')
@click.option('--model', '-m', default='text-davinici-003',
              help='The model type to use as the engine for bot.\n\nModels:\n\t- text-davinci-003\n\t- ')
@click.option('--model', '-m', default='text-davinici-003',
              help='The model type to use as the engine for bot.\n\n\tRead more here: ')
def ask(prompt, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
    bot_instance = make_bot()
    result = bot_instance.ask(prompt, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty)
    click.echo(result)

if __name__=='__main__':
    cli()
