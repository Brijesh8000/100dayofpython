from insta_collection import rohit_follower
from instabot import Bot

bot = Bot()

# bot.login(username="mg416.brijesh",password="Bks8000")
my_followers = bot.get_user_followers("rohittt_09_")
for follower in my_followers:
    rohit_follower.append(follower)


