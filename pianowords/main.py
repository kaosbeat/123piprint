import sys
sys.path.append('lib')
from filestuff import *
import random
import math
import os
import midiparser as mp
import musicconcepts as mc
import songtext
import assoc
import speak


# fix for http://stackoverflow.com/questions/31137552/unicodeencodeerror-ascii-codec-cant-encode-character-at-special-name
# reload(sys)
# sys.setdefaultencoding('utf-8')

assoc.initAssoc()
#######
print("##################################")
# sentence = songtext.sentence
# for x in range(0,10):
# 	sentence = songtext.testsentence(sentence)





def sayhello():
	print("Hello, how are you")
	print("sure is" + songtext.getweather()["temp"]  + "at" + mc.sessionvars["songlocation"] )
	print("I'm sorry I only speak English")
	print("But I'm not listening to you anyway")
	print("My settings are:")
	print("maximum songlength: " +str(mc.sessionvars["maxsonglength"]))
	print("maximum silence in song: " + str(mc.sessionvars["maxsilencetime"]))
	print("so far I learned "+ str(mc.sessionvars["wordcount"])+ " words")


mc.sessionvars["songlocation"] = "de Krook"
# assoc.fetchandstorewords(["nourish"], assoc.confirmedwordlist)
songtext.updateobjectcount()
sayhello()

while True:
	# check if we need to end a song and start endprinter
	mc.checkSongEnd()
	pass