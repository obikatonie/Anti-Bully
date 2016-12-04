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

for status in tweepy.Cursor(api.home_timeline).items(3):
    # print (status.text.encode('utf-8')+"\n")
    api.update_status("@123bananabot test reply", status.id)

print ("finished")
