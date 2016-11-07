from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance
import random, os
import tweepy

api_key = "<your api key here>"
api_secret = "<your api secret here>"
oauth_token = "<your oauth token here>"
oauth_token_secret = "<your oath token secret here>"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

firstPath = random.choice(os.listdir("photos"))
secondPath = random.choice(os.listdir("photos"))
firstImage = Image.open("photos/" + firstPath)
secondImage = Image.open("photos/" + secondPath)
firstEnhancer = ImageEnhance.Brightness(firstImage)
secondEnhancer = ImageEnhance.Brightness(secondImage)
blend = ImageChops.add(firstEnhancer.enhance(0.8), secondEnhancer.enhance(0.7))
blend.save('Blend.jpg')

api.update_with_media("Blend.jpg")
