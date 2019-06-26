import datetime
import songtext
miditimesongstart = datetime.datetime.utcnow()
miditimelastnote = datetime.datetime.utcnow()
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



# def TimestampMillisec64(c):
# 	# print(datetime.datetime.utcnow().microsecond)
# 	# print(miditime.microsecond)
# 	# return int((datetime.datetime.utcnow() - miditime).total_seconds() * 1000) 
#     # return int((datetime.datetime.utcnow().microsecond - miditime.microsecond)*1000) 
# 	return (datetime.datetime.now() - )


def resetSeqs():
	global miditimesongstart
	global msgs
	global seqNotes
	global seqNotesOn
	global seqNotesOff
	global seqVelocityOn
	global seqVelocityOff
	global seqDeltaOn
	global seqDeltaOff
	miditimesongstart = datetime.datetime.utcnow()
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



def dostuff(msg):
	global miditimesongstart
	global miditimelastnote
	miditimecurrentnote = datetime.datetime.utcnow() 
	# print((miditimecurrentnote - miditimelastnote).microseconds)
		#first check if we need to restartsong
	# if ((miditimecurrentnote - miditimelastnote).microseconds > 1000000):
	# 	resetSeqs()
	# 	print("restarting song, the silence was too long")

	if ((miditimecurrentnote - miditimesongstart).total_seconds() > 5):
		resetSeqs()
		print("restarting song, the song has been playing too long", (miditimecurrentnote - miditimesongstart).microseconds)
				
		

	# timestamp = TimestampMillisec64()
	# print(timestamp)
	try:
		addToSeqs(msg.note, msg.velocity, msg.type, (datetime.datetime.utcnow() - miditimesongstart))
		# print (TimestampMillisec64())
	except AttributeError:
		pass

	# print("callback called")
