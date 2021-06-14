#6/10/21: combine both the reddit and twitter functionality into one program
#6/11/21 : adjusted char count for titles
#To do:
#   get all access keys into here
#   paste working twitter and reddit scripts
#   adjust twitter script to post the reddit info
#   may have to adjust how long the title are. need to be less than 280

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
for submission in subreddit.hot(limit=5):
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
        #gets the contents of Submission
        print("Content: \n" + submission.selftext)
        #gets image
        #not sure if i even need this
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
        counter+=1















#creating a array to hold some values; will post them to twitter
array = ["Hello World!!", "This is my second tweet", "Third ", "Fourth", "Fifth"]
#cannot upload duplicate posts

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

print("Completed!  " + user.name)
