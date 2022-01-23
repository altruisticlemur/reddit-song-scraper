import praw
from praw.models import MoreComments
import random
import time

def bot_login():
    print ("Logging in...")
    r = praw.Reddit(
        client_id="client_id",
        client_secret="client_secret",
        user_agent="u/altrustic_lemur",
        username="altrustic_lemur",
        password="password",
    )
    print ("Logged in!")
    return r

def run_bot(r, comments):
    url = "https://www.reddit.com/r/AskReddit/comments/s9oaa6/what_is_the_most_beautiful_song_you_have_ever/"

    submission = r.submission(url=url)
    submission.comments.replace_more(limit=None)
    
    for comment in submission.comments:
        comments.append(comment.id)
        try:
            with open ("comments.txt", "a+") as f:
                f.write(comment.body + "\n")
        except:
            print("fail")
		
    time.sleep(10)
    print(len(comments))

r = bot_login()
comments = []

run_bot(r, comments)
