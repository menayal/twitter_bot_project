#exampleHelloWorldBot
#Update: 4/7/21 -- downloaded praw for reddit api.
#Update: 4/18/21 -- moved to new folder, twitter bot.
#update: 4/29/21 -- imported os, dontenv to use env variables
#update: 6/10/21: created functions to be reference in the Awwducational bot.
import os
from dotenv import load_dotenv #need this to access env variables
import tweepy
import time

load_dotenv() #load the environment variables from .env

#can probably hold these values in another file for them to be safer
#twitter access keys
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.getenv('TWITTER_ACCESS_KEY')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#use this to call twitter api
twitter_API = tweepy.API(auth)
#twitter_API.update_status("hello world") Cause the tweet to be tweeted with words "hello world"
user = twitter_API.me()


#creating a array to hold some values; will post them to twitter
array = ["Hello World!!", "This is my second tweet", "Third ", "Fourth", "Fifth" ]
#cannot upload duplicate posts

#  whatever the time to sleep is
# while True:
#     time.sleep(3600) ## in seconds i think

#print to twitter
flag = True
while flag:
    #will print the values in the array every min(60sec) to twitter
    for string in array:
        #prints out the element string
        #twitter_API.update_status(string)
        print(string)
        #time.sleep(60)
        time.sleep(10)
    flag = False

print("Completed!  " + user.name )
