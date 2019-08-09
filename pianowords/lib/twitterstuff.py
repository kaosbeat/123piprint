import sys
import tweepy
import authkeys
  
# authentication 
auth = tweepy.OAuthHandler(authkeys.consumer_key, authkeys.consumer_secret) 
auth.set_access_token(authkeys.access_token, authkeys.access_token_secret) 
   
api = tweepy.API(auth) 

def tweetsong(image_path):
# to attach the media file 
#status = 
    tweet = "testing"
    api.update_with_media(image_path, tweet)  
# api.update_status(status = tweet) 
