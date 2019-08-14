import sys
from contextlib import suppress
import songtext
import tweepy
import authkeys
import re
import filestuff
import threading
import sh

# tweetvars = {}
# tweetvars['sinceID'] = 1158415586206113792 #should alway be bigger then maxsilencetime
tweetvars = filestuff.file2Object("tweet.store")
# filestuff.object2File(songtext.songs, "songs.store")
# songtext.songs = {}

# tweetvars['sinceID'] = 1158415586206113792 #should alway be bigger then maxsilencetime

# print(songtext)

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


def lookfornewtexts():
	global tweetvars
	search = tweepy.Cursor(api.search, q="#123piano #inspiration", since_id=tweetvars["sinceID"], lang="en").items(50)
	for item in search:
		print(api.get_user(item.user.id).screen_name)
		text = parseTweetToSongText(item.text, item.entities['hashtags'])
		user = api.get_user(item.user.id).screen_name
		print(item.id)
		if (item.id > tweetvars["sinceID"]):
			tweetvars["sinceID"] =  item.id
		storenewsongtext(text, user, tweetvars["sinceID"])
		print("storing text")
		#"now do git commit?"
		# add a file
		# print repo.git.add( 'somefile' )
		# print(git.commit( m="the sinceID = " +str(tweetvars["sinceID"]) ))
		# print(text.encode('utf-8'))
		tweetReply(tweetvars["sinceID"] )
		# for w in stuff:
			# print(w.encode('utf-8'))
	#store updates back to the object
	# remove the line below to activate real storing etc
	# tweetvars["sinceID"] = 1158415586206113792
	filestuff.object2File(tweetvars, "tweet.store")
	git = sh.git.bake(_cwd='/home/pi/123piprint')
	git.add("*")
	git.commit( m="new " +str(tweetvars["sinceID"]) )
	git.pull("--commit")
	git.push()

def parseTweetToSongText(tweet, hashtags):
	# song = '05 August, 2019, 17:43 This is song 347 performed at L40 on this hot day #123piano @kaosbeat https://t.co/hPJPjufSGq'
	# song = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
	processedsong = []
	song = re.sub(r"http\S+", "", tweet)
	song = song.split()
	print("unhanshtagremovedsong")
	print (song)
	for tag in hashtags:
		with suppress(ValueError, AttributeError):
			print(tag["text"])
			song = song.remove(tag["text"])
			
	for word in song:
		word = word.split(".")[0]
		word = re.sub('[!@#$\"`~%^&*()_+\-|?\/.,><;:\']', '', word)
		word = word.lower()
		processedsong.append(word)
	return processedsong

def storenewsongtext(text, user, id):
	songtext.songs[id] = {"text": text, 'user': user}
	# copyfile("songs.store", "songs.store.backup")
	filestuff.object2File(songtext.songs, "songs.store")
	return True

def tweetReply(id):
	# print("resentece")
	newsentence = songtext.resentence(songtext.songs[id]["text"])
	# print(newsentence)
	flatsentence = ""
	for word in newsentence:
		flatsentence = flatsentence + word + " "
	# print(flatsentence)
	reply = "thanks a lot for inspiring me @" + songtext.songs[id]["user"] + " if you play, it might sound like: " + flatsentence
	api.update_status(status=reply, in_reply_to_status_id=id)
	print(reply)
	return reply

class ThreadingLookForTweets(object):
	def __init__(self):
		""" 
		looks for new tweets in the background
		"""
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True                            # Daemonize thread
		thread.start()                                # Start the execution

	def run(self):
		lookfornewtexts()



