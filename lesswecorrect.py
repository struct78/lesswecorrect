#!/usr/bin/env python
# lesswecorrect.py
# A Twitter bot that corrects people who say "Less we forget" instead of "Lest we forget"
# Author : David Johnson <@struct>
 
import tweepy
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Key settings
CONSUMER_KEY 		= ""
CONSUMER_SECRET 	= ""
ACCESS_TOKEN 		= ""
ACCESS_TOKEN_SECRET	= ""

phrases = ['lessweforget', 'less we forget']

def correct(data): 
	global link, stream, num_links
	tweet = json.loads(data)
	text = tweet['text']

	if not tweet.get('retweeted_status'):
		for phrase in phrases:
			# We have to do regex match because streaming tracking doesn't allow us to match whole phrases
			if text.find(phrase):
				id = tweet['id']
				username = tweet['user']['screen_name']
				reply = 'It\'s actually "Lest We Forget", @%s' % (username)

				api.update_status(status=reply, in_reply_to_status_id=id)
				break


class TweetListener(StreamListener):
    def on_data(self, data):
    	correct(data)
       	return True

    def on_error(self, status):
        print(status)

listener = TweetListener()

# OAuth Handler
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create the API object
api = tweepy.API(auth)

# Create the stream
stream = Stream(auth, listener, gzip=True)
stream.filter(track=phrases)
stream.filter(language=['en'])