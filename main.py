import tweepy
from tweepy import OAuthHandler

consumer_key = "Duw3rXopMBHfM8OtNMy8NJLQr"
consumer_secret = "oinn6izuprljeIgXsYp48c9acvqawAE5rCnrtzqyC2bIRqeRPV"
access_token = "3058890440-7Q0qIMkrT31ZNlBpmzD77dQd2R9PLqqkcfPNcxL"
access_secret = "ukrKwrLK5NKmCt4VdIZbqLcw0aldRznlj0YIoh7ZOxaHS"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
