import praw
from config import *

if __name__ == "__main__":
    content = raw_input("1 - Text\n2 - URL\n\nWhat do you want to post: ")
    print '\n'
    title = raw_input("TITLE: ")

    if content == "1":
        body = raw_input("BODY: ")
    if content == "2":
        body = raw_input("URL: ")

    subreddit = raw_input("SUBREDDITS to SUBMIT: ")

    comment = raw_input("COMMENT: ")


    user_agent = 'PUTREDDITNAMEHERE automatic publisher.'
    r = praw.Reddit(user_agent=user_agent)

    r.login(REDDIT_USER, REDDIT_PASS)

    subreddit = subreddit.split(",")

    for sub in subreddit:
        if content == "1":
            post = r.submit(sub, title, text=body)
        if content == "2":
            post = r.submit(sub, title, url=body)
        if comment:
            post.add_comment (comment)

    print '\n'
    print ("Thank you, and I hope to see you again, " + REDDIT_USER + " :)")
