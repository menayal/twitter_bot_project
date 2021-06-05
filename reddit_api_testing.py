#4/18/21: imported praw, Adding authentication; got title, source, content, submission points to.
#4/29/21: imported os, dotenv for env variables. Example in testing.py
#5/2/21: imported urllib.request//not working
#6/4/21: used requests to download the pictures to the pic dir successfully
#TO DO:
# Combine the reddit portion and twitter portion to post on twitter.
# automate on a remote server.
# Possible problems may be deleting the files after downloading and posting
# to twitter.

import os
from dotenv import load_dotenv #for use of env variables
load_dotenv() #take the environment variables from .env
import praw
import pprint #used this to learn more about the attributes in objects
import urllib #used to download picture
import requests

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
)
#Seeing if i am auhenticated correctly; works correctly
print("User: " + str(reddit.user.me()))
print("Processesing: \n")


#get a subreddit post
subreddit = reddit.subreddit("Awwducational")
#get top 5 hottest posts in nba subreddit; 2 posts are sticked
#counter
counter = 1
for submission in subreddit.hot(limit=3):
    if not(submission.stickied):
        print("#" + str(counter) + " Title: \t" + submission.title + "\n")
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




#check attrubutes
#pprint.pprint(vars(submission))
print("\nComplete")
