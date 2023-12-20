from bot import make_bot

bot = make_bot()
# print(bot.resize_image_4mb('photos/reid.jpg'))
print(bot.recreate_image('photos/reid.jpg', n=3))