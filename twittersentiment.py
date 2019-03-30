import tweepy
from textblob import TextBlob
import csv

consumer_key = '9KAxfAToUx4sLZnUJBYOyeXcs'
consumer_secret = 'gqDNwtb9CQ4qDRss6DCpFz4NWdMAuWfwK4eUWHsD0bYiivVhXB'

access_token = '1001802942649860096-RLl9ERDHDpQNwdKnKZlBftNQYZPLAG'
access_token_secret = 'criXD3LIp57qJkAfdMGyxYTqlmYdAyG5bkZwv1fw31mav'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Cheyne')

for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    

