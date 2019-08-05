import threading
import time
import pyttsx3
import festival
import ctypes
talking = 0
import subprocess
import musicconcepts as mc

# ttsengine = "festival"
ttsengine = "espeak"

ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int,
									  ctypes.c_char_p, ctypes.c_int,
									  ctypes.c_char_p)


def py_error_handler(filename, line, function, err, fmt):
	pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

try:
	asound = ctypes.cdll.LoadLibrary('libasound.so.2')
	asound.snd_lib_error_set_handler(c_error_handler)
except OSError:
	pass

def onStart(name):
	global talking
	# print( 'starting', name)
	talking = 1
def onWord(name, location, length):
	# print( 'word', name, location, length)
	pass
def onEnd(name, completed):
	global talking
	talking = 0
	print ("Talking Stopped")


# ##engine = pyttsx3.init()
if (ttsengine == "espeak"):
	engine = pyttsx3.init('espeak')
	engine.setProperty('rate', 150)
	engine.connect('started-utterance', onStart)
	engine.connect('started-word', onWord)
	engine.connect('finished-utterance', onEnd)
	# engine.say('The quick brown fox jumped over the lazy dog.')
	engine.runAndWait()

	def sayword(word):
		global engine
		global talking
		talking = 1
		if engine.isBusy():
			time.sleep(0.1)
		engine.say(word)
		engine.runAndWait()

def espeak(text: str, pitch: int=50) -> int:
	""" Use espeak to convert text to speech. """
	print(str(mc.speakerpitch))
	return subprocess.run(['espeak', '-p', str(mc.speakerpitch), text]).returncode
   





class ThreadingSpeak(object):
	""" Threading example class
	The run() method will be started and it will run in the background
	until the application exits.
	"""

	def __init__(self, word="hello thread"):
		""" Constructor
		:type word: string
		:param word: word to say in threaded mode
		"""
		self.word = word
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True                            # Daemonize thread
		thread.start()                                # Start the execution

	def run(self):
		global talking
		talking = 1
		talking = espeak(self.word)