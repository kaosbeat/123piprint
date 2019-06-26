import requests
import pickle
import random
import re
import nltk
from authkeys import mashapekey
from filestuff import *


wordlist = []
confirmedwordlist = []
### blacklist https://www.reddit.com/r/Twitch/comments/6jdsco/is_there_a_text_file_with_all_the_blacklisted/
blacklistedwords = ['hitler','nazi','whore']
blacklistfile = open("lib/blacklist.txt", "r")

for word in blacklistfile:
    blacklistedwords.append(word.rstrip())
# print (blacklistedwords)
blacklistfile.close()

associations = {}
stopper = False
amount = 0
credits = True




# def associateandplot(longestword):
# 		if getAssociations(longestword,associations):
# 			# writeword(longestword, random.randint(-4000,4000), random.randint(-4000,4000))
# 			checkForLinks(longestword)
# 			checkForXlinks(longestword,0)
# 			# drawbar1(15)
# 		global amount
# 		amount =  amount + 1
# 		# print wordlist
# 		if (longestword == "robot"):
# 			print ("we have to stop here")
# 			global stopper
# 			stopper = True

# def checkForLinks(word):
# 	for w in wordlist:
# 		if w in associations[word]:
# 			print (w +" is really in there " )
# 			print ("and the score is :")
# 			print (associations[word][w])
# 				# ['probably']
# 			connectWords(w, word)

# 		else: 
# 			# print "nogo"
# 			return


# def checkForXlinks(word, functiontitleindex):
# 	global orderLevel
# 	print ("### looking into " + word + " order " + str(orderLevel))
# 	lowcasetitles = [x.lower() for x in functiontitle[functiontitleindex]]
# 	for w in associations[word]:
# 		print ("the word is :" + w)
# 		if w in lowcasetitles: # if match pick
# 			print ("title is : " + w)
# 			output3.append(w)
# 			return
# 		else: 
# 			# if no match pick first assoc with median score and get assocs
# 			# nextorderword = (associations[word].keys()[associations[word].values().index((sorted(associations[word].values()))[int(len(associations[word])/2)])])
# 			# if no match pick random assoc 
# 			nextorderword = (associations[word].keys()[associations[word].values().index((sorted(associations[word].values()))[random.randint(0,len(associations[word]))-1])])
# 			# pick best match
# 			# nextorderword = (associations[word].keys()[associations[word].values().index((sorted(associations[word].values()))[0])])
# 			print (associations[word].keys())
# 			print ((sorted(associations[word].values()))[0])
# 			print(nextorderword)
# 			if nextorderword in lowcasetitles:
# 				print (" nextordertitle is : " + nextorderword)
# 				output3.append(nextorderword)
# 				return
# 			# print (keys(associations[word]))
# 			orderLevel = orderLevel + 1
# 			if orderLevel < 3:
# 				if getAssociations(nextorderword,associations):
# 					checkForXlinks(nextorderword, functiontitleindex)
# 			else:
# 				# print ("finalnextordertitle is : " + (functiontitle[functiontitleindex][random.randint(0,len(functiontitle[functiontitleindex]))]))
# 				# output3.append(functiontitle[functiontitleindex][random.randint(0,len(functiontitle[functiontitleindex]))])
# 				output3.append(nextorderword)
# 			return
# 			# print ("nolink")	



def getAssociations(word,associations):
	r = requests.post("https://twinword-word-associations-v1.p.mashape.com/associations/",
	  headers={
	    "X-Mashape-Key": mashapekey,
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Accept": "application/json"
	  },
	  params={
	    "entry": word
	  }
	)
	response = r.json()
	print(response['result_code'])
	if (response['result_code'] == '200'):
		print(response)
		print(response['associations_scored'])
		associations.update({word: response['associations_scored']})
		return True

	else:
		print(response['result_msg'])
	
	# if word in associations:
	# 		print ("the score for " + word + " = " )
	# 		print (associations[word][unicode])])

# def dump2file(object, filename):
# 	f=open(filename, 'wb')
# 	pickle.dump(object, f)
# 	f.close()





def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


def fetchandstorewords(wordlist, confirmedwordlist):
	wordlist = uniq(wordlist)
	for word in wordlist:
		word = re.sub('[!@#$"`~%^&*()_+-}]{[|?/.,><;:\']', '', word)
		# word.translate(None, '!@#$"`~%^&*()_+-}]{[|?/.,><;:\'')
		# check associations
		filename = 'objects/' + word + '.assoc'
		# print(filename)
		if not os.path.isfile(filename):
			print("going online")
			if not getAssociations(word,associations):
				print ("not an easy word :" + word)
				associations[word] = None
				print("writing None object to disk")
				object2File((associations[word]), filename)
			else:
				#prepend list with baseword
				print("writing  " + word + " to disk")
				object2File((associations[word]), filename)
				# if (word == checkIfNounOnDiskOrGet(word)):
				confirmedwordlist.append(word)

		else:
			print("found "+ word + " on disk" )
			associations[word] = file2Object(filename)
			confirmedwordlist.append(word)
			print ("unpickled")
			print (associations[word])
			# print (confirmedwordlist)
		
	
	#remove blacklisted words
	for bw in blacklistedwords:
		while bw in confirmedwordlist: confirmedwordlist.remove(bw)


# print(getAssociations('hello',associations))



def getTypeFromAssoc(word,wordtype):
	# typelist = []
	wordlist = []
	taggedlist2 = []
	# print (associations[word])
	if (associations[word] != None):
		for w in associations[word]:
			# wordlist.append(w)
			taggedlist2.append(nltk.pos_tag([w])[0])
		# taggedlist = (nltk.pos_tag(typelist))
		#different approach, single POS tag vs "sentencetagging"
		# print (taggedlist)
	else:
		print("we have a None object")
	#### our wordlist
	# print (taggedlist2)

	for wordtag in taggedlist2:
		if (wordtag[1] == wordtype):
			wordlist.append(wordtag[0])
	if (len(wordlist) != 0):
		# print(wordlist)
		return wordlist
	else:
		return [word]




####
# init assoc files needed
def initAssoc():
	global wordlist
	global associations
	#load known wordlist
	loadObjectsDirectory2wordlist('objects/', wordlist)
	# print (wordlist)
	fetchandstorewords(wordlist, confirmedwordlist)
	# print(associations)
	# print(associations['vortex'])
	#print('###################################')
	# print(nltk.pos_tag(confirmedwordlist))
	# for word in associations['vortex']:
	# 		print(word)
			# print(word[0])
			# taggedword = nltk.pos_tag(word)
			# print(taggedword)
	#load tracery objects
	# print(getTypeFromAssoc('vortex','NN'))




