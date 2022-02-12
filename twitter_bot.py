
import os
from dotenv import load_dotenv #need this to access env variables
import tweepy
import time

load_dotenv() #load the environment variables from .env

#twitter access keys
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.getenv('TWITTER_ACCESS_KEY')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#use this to call twitter api
twitter_API = tweepy.API(auth)
#twitter_API.update_status("hello world") Causes the tweet to be tweeted with words "hello world"
user = twitter_API.me()


#creating a array to hold some values; will post them to twitter
array = ["Hello World!!" ]
#cannot upload duplicate posts

#print to twitter
flag = True
while flag:
    #will print the values in the array every min(60sec) to twitter
    for string in array:
        #prints out the element string
        #twitter_API.update_status(string)



        #test out replying to tweet first then use media; pain text works!
        # original_tweet = twitter_API.update_status(status="plain text 0.0")
        # reply_tweet = twitter_API.update_status(status="plain text reply 1", in_reply_to_status_id=original_tweet.id,auto_populate_reply_metadata=True)

        #upload media
        media = twitter_API.media_upload("pic/mhefwskph8371.gif")
        #upload media tweet works!
        original_tweet = twitter_API.update_status(status="media with text 0.0", media_ids=[media.media_id])
        reply_tweet = twitter_API.update_status(status="media text reply 1", in_reply_to_status_id=original_tweet.id,auto_populate_reply_metadata=True)



        print(string)
        #time.sleep(60)
        time.sleep(10)
    flag = False

print("Completed!  " + user.name )
