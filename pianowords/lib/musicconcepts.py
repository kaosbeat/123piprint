import datetime
import time
import songtext
import threading
import filestuff
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
speakerpitch = 50
# voice = "-ven-us+f1 -s450"
voice = "en-us+f1"
lastnote = 64
polyvoicy = False
# sessionvars = { "songnumber": 0, "songlocation": "L40", "maxsilencetime": 3, "maxsonglength": 10}
# object2File(sessionvars, "session.store")
sessionvars = filestuff.file2Object("session.store")
sessionvars['minsonglength'] = 20 #should alway be bigger then maxsilencetime
sessionvars['maxsonglength'] = 300
sessionvars['maxsilencetime'] = 10
sessionvars["charpagewidth"] = 56
filestuff.object2File(sessionvars, "session.store")

print(sessionvars)

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
			print("silencetime = " + str((now - miditimelastnote).total_seconds()))
			if ((now - miditimesongstart).total_seconds() < sessionvars["minsonglength"]):		
				print("before I print anything, you have to play a little longer...", (now - miditimesongstart).microseconds)
				speak.ThreadingSpeak("before I print anything, you have to play a little longer...")
				playstate = False
			else:
				
				print("stopping song, the silence was too long")
				speak.ThreadingSpeak("thank you so much for playing with me, I think it was inspiring")
				songtext.stopSong()
				playstate = False
		elif ((now - miditimesongstart).total_seconds() > sessionvars["maxsonglength"]):
			print("stopping song, the song has been playing too long", (now - miditimesongstart).microseconds)
			songtext.stopSong()
			playstate = False


def dostuff(msg):
	global miditimesongstart
	global miditimelastnote
	global miditimecurrentnote
	global playstate
	global speakerpitch
	global lastnote
	global lastnotecount
	global polyvoicy
	now = datetime.datetime.utcnow()
	if (msg.type == 'note_on'):
		print(msg.note)
		speakerpitch = msg.note
		if (msg.note == 96):
			if lastnote == msg.note:
				print("lastnoet was a hit")
				lastnotecount = lastnotecount + 1
				if lastnotecount > 3:
					polyvoicy = True
		else: 
			lastnotecount = 0
		lastnote = msg.note
		if playstate:
			miditimelastnote = miditimecurrentnote
		else: 
			# resetSeqs()
			miditimelastnote = now
			miditimesongstart = now
			playstate = True
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


