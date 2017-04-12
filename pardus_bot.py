#! /usr/bin python

import tweepy
from time import  sleep


consumer_key="your consumer key"
consumer_secret="your consumer secret"

access_token="your access token"

access_token_secret="your a.t. secret "
kull_login=tweepy.OAuthHandler(consumer_key,consumer_secret)
kull_login.set_access_token(access_token,access_token_secret)
api=tweepy.API(kull_login)



try :
  #pardus etiketi altındaki tweetleri tw yapar
  for status in tweepy.Cursor(api.search,q="#Pardus").items(1000):
    api.retweet(status.id)

    sleep(5)



except tweepy.TweepError as e :
        print(e)
    #bir hesabın tweetlerini tr yapmak için 
    try :
 user_timeline=api.user_timeline(screen_name="takipedilecekhesabınismi",count=1000)

 for tivit in user_timeline:
    api.retweet(tivit.id)
    sleep(5)

except tweepy.TweepError as e :
        print(e)


