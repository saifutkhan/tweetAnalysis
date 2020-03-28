# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:50:33 2018
Copy Right
@author: skhan
version 1: gather tweets           
"""
import tweepy
import json

def tweetsToJson(tweets, filename):
    k=0
    for tweet in tweets:
        try:
            k=k+1
            f=open(filename,'a+')
            line=tweet._json
            json.dump(line,f)
            f.write('\n')
            f.close()
        except Exception as err:
            print(err)
            f.close()
    return k

consumerKey='eIai8dvFeGI9yzLpCe4RlKrQe'
consumerSecret='kpQnIPVod1aKvx0dWEAeFS4NrxPzK01T0QtNxnMFzwyAR6gZG3'
accessToken='1178934720450703360-8fISwPQCNiyEnU2rVCiC9RPrb1lJbp'
accessTokenSecret='EO1wqOXk0hC5pGyGEbR8mGrf4FO50AbbBcouiDwu1QgID'

auth=tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)

api=tweepy.API(auth)

# tweets from querying general tweets
# Replace line below with your query
#tweets=tweepy.Cursor(api.search, q='gold stock OR gold spot price OR gold dollar', lang='en', tweet_mode="extended", since='2020-03-15').items(5)
    
# gather tweets from gold news site
# do not uncomment this line for later use item=api.get_user("KitcoNewsNOW")
tweets=tweepy.Cursor(api.user_timeline, id="KitcoNewsNOW", since='2020-03-27').items(15)
numtweets=tweetsToJson(tweets,'goldtweets-saif.json')
print(numtweets)


    