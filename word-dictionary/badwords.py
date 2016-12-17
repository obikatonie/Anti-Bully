#!/usr/bin/env python

import string

badwords = []
for line in open("badwords.txt"):
    for word in line.split( ):
        badwords.append(word)

import tweepy
from tweepy import OAuthHandler

# set up api keys
consumer_key = "Duw3rXopMBHfM8OtNMy8NJLQr"
consumer_secret = "oinn6izuprljeIgXsYp48c9acvqawAE5rCnrtzqyC2bIRqeRPV"
access_token = "3058890440-7Q0qIMkrT31ZNlBpmzD77dQd2R9PLqqkcfPNcxL"
access_secret = "ukrKwrLK5NKmCt4VdIZbqLcw0aldRznlj0YIoh7ZOxaHS"

# set up auth and api
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for status in tweepy.Cursor(api.home_timeline).items(1):
    print "tweet: "+ status.text.encode('utf-8')
    # get rid of punctuation
    tweet = status.text
    tweet = "".join(l for l in tweet if l not in string.punctuation)
    tweet = tweet.lower()
    bullying = False
    for word in tweet.split(" "):
        if word in badwords:
            print "bullying"
            api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)", status.id)
            bullying = True
            break
    if bullying == False:
        api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", status.id)
        print "not bullying"
