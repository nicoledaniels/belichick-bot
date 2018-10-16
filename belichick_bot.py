import praw
import re
import os
import time

# Create the Reddit instance and log in
reddit = praw.Reddit('bot')

# Create a list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# Or load the list of comments we have replied to
else:
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

# Pull the latest 1000 comments from a chosen subreddit 
subreddit = reddit.subreddit('testingground4bots')
for comment in subreddit.comments(limit=1000):

    # Make sure you didn't already reply to this comment and it includes the provided text
    if comment.id not in comments_replied_to and re.search("belichick says", comment.body, re.IGNORECASE):
      comment.reply("bot responding!")
      print("Bot replying to : ", comment.body)

      # Store id in list
      comments_replied_to.append(comment.id)

# Write updated list to file
with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + "\n")
