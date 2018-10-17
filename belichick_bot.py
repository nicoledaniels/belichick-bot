# -*- coding: utf-8 -*-
# Weird encoding stuff

import praw
import re
import os
import random

# Create the Reddit instance and log in
reddit = praw.Reddit('bot')

# Iconic quotes
billsQuotes=["I don’t Twitter, I don’t MyFace, I don’t Yearbook","Twitter account, InstantFace, I don’t have any of that","I don’t know. MyFace, YourFace, InstantFace","Not on SnapFace, not too worried what they put on InstaChat","You get the job done or you don’t","Do your job","Knowing you have a good backup long snapper allows you to sleep good at night","What the hell is that?","Well, umm…he’s a good player. We have a lot of good players","I’m a football coach. I’m not a doctor","We're on to Cincinnati","You Sure That’s the Question You Want to Ask?","We did what we did","What do you think?","I don’t know","They were inactive so they didn't play","Seattle. Seattle. Seattle. Seattle. Seattle"]

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
      # Generate a random quote number
      random_quote_index = random.randint(0, len(billsQuotes) - 1)

      # Set the random quote
      quote = billsQuotes[random_quote_index]

      bot_signature_text = "^(I'm a bot! Message me if you have a spicy Belichick quote you want to add)"

      print("Bot replying to : ", comment.body)
      comment.reply(quote + "\n" + "***" + "\n" + bot_signature_text)

      # Store id in list
      comments_replied_to.append(comment.id)

# Write updated list to file
with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + "\n")
