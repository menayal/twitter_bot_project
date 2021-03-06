import os
from dotenv import load_dotenv #for use of env variables
import praw
import requests

load_dotenv() #take the environment variables from .env
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
)


#Seeing if i am auhenticated correctly; works correctly
print("User: " + str(reddit.user.me()) + " is authenticated\n")
print("Processesing: \n")


#get a subreddit post
subreddit = reddit.subreddit("Awwducational")
#get top 5 hottest posts in subreddit; 2(looks like 1 now) posts are sticked
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
        if (submission.url.endswith(('.jpg', '.png', '.gif', '.jpeg'))):
            print("Picture url: " + submission.url)
            #img url
            img_url = submission.url
            #file name
            filename = img_url.split("/")[-1]
            #download the file to pic dir
            r = requests.get(img_url)
            # "pic/"+filename will be the media tweeted out
            with open("pic/"+filename, "wb") as f:
                f.write(r.content)
        counter+=1


print("\nComplete")
