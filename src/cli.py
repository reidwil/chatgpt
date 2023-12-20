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

@cli.command()
@click.option('--image-path', '-p',
              help='Path to the file you want to recreate')
@click.option('--number','-n', default=3,
              help="The number of pictures to make")
@click.option('--download', '-d',  is_flag=True, show_default=True, default=False, 
              help='Should the recreated images be download')
@click.option('--path', default="./photos", help="The file path to download the drawings to")
def recreate_image(image_path, number, download, path):
    bot = make_bot()
    click.echo("Generating recreated image results...")
    result = bot.recreate_image(image_path=image_path, n=number)
    if download:
        if '/' in image_path:
            prompt = str(image_path).split('/')[-1]
        else:
            prompt = str(image_path)
        bot.download(prompt=prompt, draw_payload=result, download_path=path)
    click.echo(result)

if __name__=='__main__':
    cli()
