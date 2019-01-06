from instabot import insta

# Instagram username here
username = ""

# Instagraam password here
password = ""

# Initialize the class
bot = insta.InstagramBot(username, password)
bot.login()
hashtags = ['csgo', 'counterstrike']

while True:
    try:
        tag = insta.random.choice(hashtags)
        bot.like_photo(tag)
    except Exception:
        bot.closeBrowser()
        insta.time.sleep(60)
        bot = insta.InstagramBot(username, password)
        bot.login()
