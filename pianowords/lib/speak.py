import threading
import time

talking = 0
import subprocess
import musicconcepts as mc

def espeak(text: str, pitch: int=50) -> int:
	""" Use espeak to convert text to speech. """
	# print(str(mc.speakerpitch))
	return subprocess.run(['espeak', '-p', str(mc.speakerpitch), text]).returncode



class ThreadingSpeak(object):
	def __init__(self, word="hello thread"):
		""" 
		:type word: string
		:param word: word to say in threaded mode
		"""
		self.word = word
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True                            # Daemonize thread
		thread.start()                                # Start the execution

	def run(self):
		global talking
		if mc.polyvoicy:
			talking = 0
		else:
			talking = 1
		talking = espeak(self.word)

