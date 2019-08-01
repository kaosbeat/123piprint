import tracery
import songtext
from assoc import *
import random
from tracery.modifiers import base_english
import datetime
from weatherstuff import getweather 
import filestuff
currentsongtext = []
currentprint = []
import string
import subprocess
import threading
import musicconcepts as mc

virtualprint = True
tweeting = True

banner = """ 
       ________________________________________________________  
      /                                                       /|
     /_______________________________________________________/ |
    |                                                       |  |
    |                                                       |  |
    |   _   _       _   _   _       _   _       _   _   _   |  /
    |__//|_//|_____//|_//|_//|_____//|_//|_____//|_//|_//|__| /|
   /  /// ///  /  /// /// ///  /  /// ///  /  /// /// ///  / / |
  /  ||/ ||/  /  ||/ ||/ ||/  /  ||/ ||/  /  ||/ ||/ ||/  / /  |
 /___/___/___/___/___/___/___/___/___/___/___/___/___/___/ /|  |
 |___|___|___|___|___|___|___|___|___|___|___|___|___|___|/ |  |
    |                                                       |  |
    |                    123-PIANO                          |  |
    |                 []<> kaotec 2019                      | /
    |_______________________________________________________|/
"""

endbanner = """
 @kaosbeat #123piano
 """

#init objects
# # feed = ['feed']
# filestuff.object2File(feed, 'tracery/feed.trace')




def loadObjectsFromDisk():
    global feed
    feed = filestuff.file2Object('tracery/feed.trace')
    print(feed)

# def addAssoc2Object(object, level):



#songtitle vars



def songtitle():
    songdate = datetime.datetime.now().strftime("%d %B, %Y, %H:%M")
    introtext =  "This is song " + str(mc.sessionvars["songnumber"]) + " performed at " + mc.sessionvars["songlocation"]  + " on this " + getweather()["temp"] + " day" 
    return (songdate + " " + introtext)

def updateobject(obj, objtype):
    global confirmedwordlist
    #get assocs
    fetchandstorewords(obj, confirmedwordlist)
    # print(obj)
    newobj = {}
    for w in obj:
        newobj = newobj + getTypeFromAssoc(w,objtype)
    # print (newobj)

    

loadObjectsFromDisk()


# print(nltk.pos_tag(["feed","me","weird","music","and","I","will","grow","a","beard","filled","with","riddles","and","it","will","flow","and","grow","like","a","waterfall","grows","from","a","glacier","that","melts","like","it's","2018"]))


def testsentence(sentence):
    fetchandstorewords(sentence, confirmedwordlist)
    taggedsentence = nltk.pos_tag(sentence)
    # print(taggedsentence)
    # print(taggedsentence)
    newsentence = []
    for word in taggedsentence:
        wordlist = getTypeFromAssoc(word[0],word[1])
        # print("printing new words")
        # print(wordlist)
        newsentence.append(random.choice(wordlist))
    # print("printing new sentence")
    # print (newsentence)
    return newsentence

def resentence(sentence):
    fetchandstorewords(sentence, confirmedwordlist)
    taggedsentence = nltk.pos_tag(sentence)
    # print(taggedsentence)
    # print(taggedsentence)
    newsentence = []
    for word in taggedsentence:
        wordlist = getTypeFromAssoc(word[0],word[1])
        # print("printing new words")
        # print(wordlist)
        newsentence.append(random.choice(wordlist))
    # print("printing new sentence")
    # print (newsentence)
    return newsentence

def convertSentenceToTraceobj(tracename, sentence, traceobj):
    trace = ""
    # print(traceobj)
    for idx, word in enumerate(sentence):
        #split modifiers
        mods = None
        word = word.split(".")[0]
        word = re.sub('[!@#$\"`~%^&*()_+\-|?\/.,><;:\']', '', word)
        word = word.lower()
        if "." in word:
            mods = word.split(".")[1:len(word.split("."))]
            # print(mods)
            word = word.split(".")[0]
        #try assocs
        try: 
            associations[word]
        except:
            fetchandstorewords([word], confirmedwordlist)

        if (associations[word] != None):
            traceobj[word] = []
            for w in associations[word]:
                traceobj[word].append(w)

            if mods != None:
                # print (mods)
                for mod in mods:
                    word = word + "." + mod
            word = "#" +  word + "#"
        trace = trace + word + " "
    traceobj[tracename] = [trace]
    # print (traceobj)
    return traceobj 

def makeSense(traceobj,tracename):
    grammar = tracery.Grammar(traceobj)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#"+tracename+"#")



class getnewsongtextThread(object):
    """ Get New Songtext
    Will be run in background
    """

    def __init__(self, remangle=True):
        """ 
        remangle boolean, go fetch new words or not?
        """
        self.remangle = remangle
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                # Start the execution

    def run(self):
        getnewsongtext(self.remangle)

def getnewsongtext(remangle):
    # print("newsongtext called")
    global sentences
    global sentence
    global currentsongtext
    global currentprint
    sentence = sentences[random.randint(0,len(sentences)-1)]
    if remangle:
        sentence = resentence(sentence)
    traceme = {}
    tracename = "test"
    traceme = convertSentenceToTraceobj(tracename, sentence, traceme)
    currentsong = makeSense(traceme,tracename)
    # currentprint.append(currentsong)
    currentsongtext = currentsong.split(" ")

    # for word in currentsongtext:

    currentprint.append('\n')
    # print (currentsong)

def initSong():
    global currentprint
    global banner
    currentprint = []
    currentprint.append(songtitle())
    currentprint.append(banner)
    getnewsongtextThread(True)

def stopSong():
    global currentprint
    global virtualprint
    global endbanner
    # print("trying to print to printer")
    # print(currentprint)
    filestuff.txt2file(currentprint, "prints/song" + str(mc.sessionvars["songnumber"]) +".txt")
    currentprint.append(endbanner)
    if virtualprint:
        print(currentprint)
        print("##############################")
    else:
        subprocess.run(["lp", "-o", "cpi=24", "-o", "lpi=14" "prints/song" + str(mc.sessionvars["songnumber"]) +".txt"])
    if tweeting:
        cattext = subprocess.Popen(('cat', "prints/song" + str(mc.sessionvars["songnumber"]) +".txt"), stdout=subprocess.PIPE)
        subprocess.check_output(('convert', '-pointsize', '10', '-font', 'Courier', '-fill', 'black', 'text:-',  "prints/song" + str(mc.sessionvars["songnumber"]) +".png"), stdin=cattext.stdout)
        cattext.wait()


sentence = []
# sentencesources: "https://www.sputnikmusic.com/list.php?memberid=434091&listid=61442"
sentences = [
             ["feed","me","weird","music","and","I","will","grow","beard.a","fill.ed","with","riddle.s","and","it","will","flow","and","grow","like","waterfall.a","grows","from","glacier.a","that","melts","like","it", "is","2019"],
             ["hello", "dear", "musician"],
             ["feed","me","weird","stuff"],
             ["I", "whish", "I", "have.ed", "duck", "feet"],
             ["word.s.capitalize", "come.ed", "easy"],
             ["Emancipate", "yourselve.s", "from", "mental", "slavery", "None", "but",  "ourselve.s", "can",  "free",  "our" , "minds"],
             ["We", "are", 'just', 'two', 'lost', 'souls', 'swimming', 'in', 'a', 'fish', 'bowl.'],
             ['If', 'you', 'smile', 'at', 'me', 'I', 'will', 'understand,', 'cause', 'that', 'is', 'something', 'everybody', 'everywhere', 'does', 'in', 'the', 'same', 'language'],
             ['How', 'many', 'ears', 'must', 'one', 'man', 'have', 'before', 'he', 'can', 'hear', 'people', 'cry'],
             ['All', 'you', 'need', 'is', 'love,', 'love.', 'Love', 'is', 'all', 'you', 'need.'],
             ['An', 'honest', 'man', 'his', 'pillow', 'is', 'his', 'peace', 'of', 'mind.'],
             ['Before', 'you', 'accuse', 'me,', 'take', 'a', 'look', 'at', 'yourself'],
             ['Every', 'new', 'beginning', 'comes', 'from', 'some', 'other', "beginning's", 'end.'],
             ['Fear', 'is', 'the', 'lock', 'and', 'laughter', 'the', 'key', 'to', 'your', 'heart'],
             ['All', 'of', 'us', 'get', 'lost', 'in', 'the', 'darkness,', 'dreamers', 'learn', 'to', 'steer', 'by', 'the', 'stars.'],
             ['All', 'lies', 'and', 'jest,', 'still,', 'a', 'man', 'hears', 'what', 'he', 'wants', 'to', 'hear', 'and', 'disregards', 'the', 'rest.'],
             ['And', 'in', 'the', 'end,', 'the', 'love', 'you', 'take', 'is', 'equal', 'to', 'the', 'love', 'you', 'make.'],
             ['Even', 'the', 'genius', 'asks', 'questions.'],
             ['All', 'my', 'lies', 'are', 'always', 'wishes.'],
             ['If', 'you', 'choose', 'not', 'to', 'decide,', 'you', 'still', 'have', 'made', 'a', 'choice.'],
             ["I", "would", 'rather', 'be', 'a', 'hammer', 'than', 'a', 'nail.'],
             ['If', 'we', 'were', 'blind', 'and', 'had', 'no', 'choice,', 'would', 'we', 'hate', 'each', 'other', 'by', 'the', 'tone', 'of', 'our', 'voice'],
             ['Your', 'prison', 'is', 'walking', 'through', 'this', 'world', 'all', 'alone.'],
             ['If', 'you', 'believe', 'in', 'forever,', 'then', 'life', 'is', 'just', 'a', 'one', 'night', 'stand']
            ]


