import sys
sys.path.append('lib')


from filestuff import *
import random
import math
import os
import midiparser as mp
import songtext
import assoc


# fix for http://stackoverflow.com/questions/31137552/unicodeencodeerror-ascii-codec-cant-encode-character-at-special-name

# reload(sys)
# sys.setdefaultencoding('utf-8')


songtext.songtitle()
assoc.initAssoc()
#######
print("##################################")
# sentence = songtext.sentence
# for x in range(0,10):
# 	sentence = songtext.testsentence(sentence)

# get_message
traceme = {}
tracename = "test"
traceme = songtext.convertSentenceToTraceobj(tracename, songtext.sentence, traceme)
print (traceme)
for x in range(0,10):
	songtext.makeSense(traceme,tracename)




# assoc.fetchandstorewords(["nourish"], assoc.confirmedwordlist)

while True:
	pass