import pyttsx3
import ctypes
talking False


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


# engine = pyttsx3.init()

import speake3

engine = speake3.Speake() # Initialize the speake engine
engine.set('voice', 'en')
engine.set('speed', '250')
engine.set('pitch', '99')
# engine.connect('started-utterance', onStart)
engine.connect('finished-utterance', onEnd)

# engine.say("Hello world!") #String to be spoken

def onEnd():
    global talking
    talking False
    print "Talking Stopped"


def sayword(word):
    global engine
    global talking
    talking True
    engine.say(word)
    engine.runAndWait()
    engine.talkback()



sayword("hello world")