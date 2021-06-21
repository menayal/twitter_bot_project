#6/10/21: combine both the reddit and twitter functionality into one program
#6/11/21 : adjusted char count for titles
#6/20/21: got the script to work successfully with media.
#To do:
# host with heroku or online
# post a tweet every x amount; maybe 24hrs

#twitter side libraries
import os
from dotenv import load_dotenv #need this to access env variables
import tweepy
import time

#reddit side libraries
import praw
import requests

load_dotenv() #load the environment variables from .env

#twitter access keys
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.getenv('TWITTER_ACCESS_KEY')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#reddit access keys
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
)

twitter_API = tweepy.API(auth) #use this to call twitter api
user = twitter_API.me()


#Seeing if i am auhenticated correctly; works correctly
print("User: " + str(reddit.user.me()) + " is authenticated\n")
print("Processesing: \n")

#get a subreddit post
subreddit = reddit.subreddit("Awwducational")
#get top 5 hottest posts in nba subreddit; 2(looks like 1 now) posts are sticked
#counter
counter = 1
for submission in subreddit.hot(limit=2):
    if not(submission.stickied):
        #store the submission.title in a variable
        title = str(submission.title)
        print("#" + str(counter) + " Title: \t" + title + "\n")
        print("Has " + str(len(title)) + " characters\n")

        #adjusting the title to be able to post titles longer than 280 chars
        adjustedTitle = title[0:273]
        if(len(title) > 273):
            adjustedTitle = title[0:273] + "(cont.)"
            print(adjustedTitle)

        #gets the url the post is pointing to
        print("Submissions points to \t" + submission.url )
        #gets the url of post
        print("Source URL: \t" + submission.shortlink )

        #gets image
        if (submission.url.endswith(('.jpg', '.png', '.gif', '.jpeg'))):
            print("Picture url: " + submission.url)
            #img url
            img_url = submission.url
            #file name
            filename = img_url.split("/")[-1]
            #download the file to pic dir
            r = requests.get(img_url)
            with open("pic/"+filename, "wb") as f:
                f.write(r.content)

            #print to twitter
            flag = True
            while flag:
                print("tweeting")
                # #upload media
                media = twitter_API.media_upload("pic/"+filename)
                #tweet with media and reply with source
                original_tweet = twitter_API.update_status(status= adjustedTitle, media_ids=[media.media_id])
                reply_tweet = twitter_API.update_status(status="Source: " + submission.shortlink, in_reply_to_status_id=original_tweet.id,auto_populate_reply_metadata=True)

                #will print the values in the array every min(60sec) to twitter
                #time.sleep(60)

                #should adjust to 24 hrs of sleep
                time.sleep(10)
                flag = False

            print("Completed!  " + user.name)

        #move to next post
        counter+=1
