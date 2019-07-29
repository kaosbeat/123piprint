import datetime
import time
import songtext

# import printer
import speak
miditimesongstart = datetime.datetime.utcnow()
miditimelastnote = datetime.datetime.utcnow()
miditimecurrentnote = datetime.datetime.utcnow()
msgs = []
seqNotes =  []
seqNotesOn =  []
seqNotesOff =  []
seqVelocityOn = []
seqVelocityOff = []
seqDeltaOn = []
seqDeltaOff = []
style = "basic"
level = ""
model = {}
playstate = False
cursor = 0
maxsilencetime = 3
maxsonglength = 10


# def TimestampMillisec64(c):
# 	# print(datetime.datetime.utcnow().microsecond)
# 	# print(miditime.microsecond)
# 	# return int((datetime.datetime.utcnow() - miditime).total_seconds() * 1000) 
#     # return int((datetime.datetime.utcnow().microsecond - miditime.microsecond)*1000) 
# 	return (datetime.datetime.now() - )


def resetSeqs():
	global msgs
	global seqNotes
	global seqNotesOn
	global seqNotesOff
	global seqVelocityOn
	global seqVelocityOff
	global seqDeltaOn
	global seqDeltaOff
	global playstate
	songtext.songnumber = songtext.songnumber + 1
	seqNotes =  []
	seqNotesOn =  []
	seqNotesOff =  []
	seqVelocityOn = []
	seqVelocityOff = []
	seqDeltaOn = []
	seqDeltaOff = []
	print(songtext.songtitle())
	

def addToSeqs (note, velocity, msgtype, delta):
	if (msgtype == 'note_on'):
		seqNotes.append(note)
		seqNotesOn.append(note)
		seqVelocityOn.append(velocity)
		seqDeltaOn.append(delta)
	elif (msgtype == 'note_off'):
		seqNotes.append(note)
		seqNotesOff.append(note)
		seqVelocityOff.append(velocity)
		seqDeltaOff.append(delta)
	# print (seqNotes) 

	
def calcStyle():
	if (seqNotesOn.length > 2):
		print (seqNotesOn[seqNotesOn.length-1], seqNotesOn[seqNotesOn.length-2])
		if (seqNotesOn[seqNotesOn.length-1] == seqNotesOn[seqNotesOn.length-2]):
			style = "repetetive"
		if (seqNotesOn[seqNotesOn.length-1] - seqNotesOn[seqNotesOn.length-2]  >  4 ):
			style = "extreme"
		if (seqNotesOn[seqNotesOn.length-1] - seqNotesOn[seqNotesOn.length-2]  <=  4 ):
			style = "moderate"
		if (seqNotesOn[seqNotesOn.length-1] < 43):
			level = "low"
		elif (seqNotesOn[seqNotesOn.length-1] >= 43 and seqNotesOn[seqNotesOn.length-1] <= 86):
			level = "medium"
		elif (seqNotesOn[seqNotesOn.length-1] > 86):
			level = "high"
		print(style, " ", level)

def buildWord(note, velocity):
		print(note,velocity)


def checkSongEnd():
	global miditimesongstart
	global miditimelastnote
	global miditimecurrentnote
	global playstate
	if playstate:
		now = datetime.datetime.utcnow()
		# print((miditimecurrentnote - miditimelastnote).total_seconds())
		if ((now - miditimelastnote).total_seconds() > maxsilencetime):
			playstate = False
			# printer.closePrinter()
			print("stopping song, the silence was too long")
			print("linefeed")
			songtext.getnewsongtext()
		if ((now - miditimesongstart).total_seconds() > maxsonglength):
			playstate = False
			# printer.closePrinter()
			print("stopping song, the song has been playing too long", (now - miditimesongstart).microseconds)
			print("linefeed")
			songtext.getnewsongtext()


def dostuff(msg):
	global miditimesongstart
	global miditimelastnote
	global miditimecurrentnote
	global playstate
	now = datetime.datetime.utcnow()
	if (msg.type == 'note_on'):
		fs.noteon(0, msg.note, msg.velocity)
		if playstate:
			miditimelastnote = miditimecurrentnote
		else: 
			playstate = True
			# printer.openPrinter()
			resetSeqs()
			miditimelastnote = now
			miditimesongstart = now
		miditimecurrentnote = now
		if (speak.talking == False): 
			printwordonline()
	if (msg.type == 'note_off'):
		fs.noteon(0, msg.note, msg.velocity)
	try:
		addToSeqs(msg.note, msg.velocity, msg.type, (now - miditimesongstart))
	except AttributeError:
		pass
	# print("callback called")
	
	# printer.PrintWord("hello from the piano: " + str(msg.note))

def printwordonline():
	global cursor
	try:
		a = songtext.currentsongtext.pop(0)
		cursor = cursor + len(a) + 1
		if (cursor > 80):
			cursor = 0
			# print('linefeed')
			print(a + " ")
			# printer.NextLine()
			# printer.PrintWord(a + " ")
			speak.sayword(a)
		else: 
			print(a + " ")
			# printer.PrintWord(a + " ")
			speak.sayword(a)

	except IndexError:
		print("linefeed")
		# printer.NextLine()
		cursor = 0
		songtext.getnewsongtext()
		a = songtext.currentsongtext.pop(0)
		# print(a + " ")
		# printer.PrintWord(a + " ")
		speak.sayword(a)
		cursor = cursor + len(a) + 1