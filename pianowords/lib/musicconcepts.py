import datetime
import time
import songtext
import speak
import threading
import filestuff
# import printer

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

# sessionvars = { "songnumber": 0, "songlocation": "L40", "maxsilencetime": 3, "maxsonglength": 10}
# object2File(sessionvars, "session.store")
sessionvars = filestuff.file2Object("session.store")
print(sessionvars)

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
	global sessionvars
	sessionvars["songnumber"] = sessionvars["songnumber"] + 1
	filestuff.object2File(sessionvars, "session.store")
	seqNotes =  []
	seqNotesOn =  []
	seqNotesOff =  []
	seqVelocityOn = []
	seqVelocityOff = []
	seqDeltaOn = []
	seqDeltaOff = []
	# print(songtext.songtitle())
	

def addToSeqs (note, velocity, msgtype, delta):
	global seqNotes
	global seqNotesOn
	global seqNotesOff
	global seqVelocityOn
	global seqVelocityOff
	global seqDeltaOn
	global seqDeltaOff
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
	global seqNotesOn
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
	global sessionvars
	if playstate:
		now = datetime.datetime.utcnow()
		if ((now - miditimelastnote).total_seconds() > sessionvars["maxsilencetime"]):
			playstate = False
			print("stopping song, the silence was too long")
			songtext.stopSong()
		if ((now - miditimesongstart).total_seconds() > sessionvars["maxsonglength"]):
			playstate = False
			print("stopping song, the song has been playing too long", (now - miditimesongstart).microseconds)
			songtext.stopSong()

def dostuff(msg):
	global miditimesongstart
	global miditimelastnote
	global miditimecurrentnote
	global playstate
	now = datetime.datetime.utcnow()
	if (msg.type == 'note_on'):
		# print(msg)
		if playstate:
			miditimelastnote = miditimecurrentnote
		else: 
			playstate = True
			resetSeqs()
			miditimelastnote = now
			miditimesongstart = now
			songtext.initSong()
		miditimecurrentnote = now
		if (speak.talking == 0): 
			jibberThread()
	# if (msg.type == 'note_off'):
	# 	# fs.noteon(0, msg.note, msg.velocity)
	# 	pass
	try:
		addToSeqs(msg.note, msg.velocity, msg.type, (now - miditimesongstart))
	except AttributeError:
		pass
	# print("callback called")
	


class jibberThread(object):
	""" 
	Threading get words to say online
	The run() method will be started 
	"""
	
	def __init__(self):
		""" Constructor
		fire and forget
		"""
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True                            # Daemonize thread
		thread.start()                                # Start the execution

	def run(self):
		global cursor
		global sessionvars
		sessionvars["charpagewidth"] = 56
		try:
			a = songtext.currentsongtext.pop(0)
			cursor = cursor + len(a) + 1
			# print ("printwordsonline " + str(a) + "cursor " + str(cursor))
			if (cursor > sessionvars["charpagewidth"]):
				cursor = 0
				songtext.currentprint.append('\n')
				songtext.currentprint.append(a + " ")
				speak.ThreadingSpeak(a)
			else: 
				songtext.currentprint.append(a + " ")
				speak.ThreadingSpeak(a)

		except IndexError:
			# print("indexerror linefeed")
			cursor = 0
			songtext.getnewsongtext(False)
			a = songtext.currentsongtext.pop(0)
			songtext.currentprint.append('\n')
			songtext.currentprint.append(a + " ")
			speak.ThreadingSpeak(a)
			cursor = cursor + len(a) + 1