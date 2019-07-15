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





# assoc.fetchandstorewords(["nourish"], assoc.confirmedwordlist)

while True:
	# check if we need to end a song and start endprinter
	mc.checkSongEnd()
	pass