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
for x in range(0,10):
	songtext.testsentence()
# get_message

while True:
	pass