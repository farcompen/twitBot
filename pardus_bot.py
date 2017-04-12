#! /usr/bin python

import tweepy
from time import  sleep


consumer_key="HkAvgwmkC20Osnck42vq7Hp3G"
consumer_secret="nlVF8LsZgmzINpgZNpglYa8jp4thqvKLfL7dBKx6aN1DKdikqP"

access_token="841609620699414529-8ALYrTo3Ji3ZMmAVFCALA2PhO03rxqI"

access_token_secret="JK6nqzhHQ93d7bDMgDghk6ToIaDncStpr6YF651gVMDfU"
kull_login=tweepy.OAuthHandler("HkAvgwmkC20Osnck42vq7Hp3G","nlVF8LsZgmzINpgZNpglYa8jp4thqvKLfL7dBKx6aN1DKdikqP")
kull_login.set_access_token("841609620699414529-8ALYrTo3Ji3ZMmAVFCALA2PhO03rxqI","JK6nqzhHQ93d7bDMgDghk6ToIaDncStpr6YF651gVMDfU")
api=tweepy.API(kull_login)



try :
  for status in tweepy.Cursor(api.search,q="#Pardus").items(1000):
    api.retweet(status.id)

    sleep(5)



except tweepy.TweepError as e :
        print(e)

