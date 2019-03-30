# Twitter Sentiment analysis, returning sntiment and relevant word and then printing to CSV

import tweepy
from textblob import TextBlob
import csv

consumer_key = 'XXX'
consumer_secret = 'XXX'

access_token = 'XXX'
access_token_secret = 'XXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Cheyne')

for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    

