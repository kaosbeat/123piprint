import tracery
import songtext
from assoc import *
import random
from tracery.modifiers import base_english
import datetime
from weatherstuff import getweather 
import filestuff
currentsongtext = []
import string
#init objects
# # feed = ['feed']
# filestuff.object2File(feed, 'tracery/feed.trace')




def loadObjectsFromDisk():
    global feed
    feed = filestuff.file2Object('tracery/feed.trace')
    print(feed)

# def addAssoc2Object(object, level):






#songtitle vars
songnumber = 0
songlocation = "L40"


def songtitle():
    global songnumber
    songdate = datetime.datetime.now().strftime("%d %B, %Y, %H:%M")
    return ( "This is song " + str(songnumber) + " performed at " + songlocation  + " on this " + getweather()["temp"] + " day" )

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
    print(taggedsentence)
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
    print(traceobj)
    for idx, word in enumerate(sentence):
        #split modifiers
        mods = None
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



def getnewsongtext():
    global sentences
    global sentence
    global currentsongtext

    sentence = sentences[random.randint(0,len(sentences)-1)]
    traceme = {}
    tracename = "test"
    traceme = convertSentenceToTraceobj(tracename, sentence, traceme)
    currentsong = makeSense(traceme,tracename)
    print (currentsong)
    print (len(currentsong.split(" ")))
    currentsongtext = currentsong.split(" ")
#gletcherobjects

sentence = []
sentences = [
             ["feed","me","weird","music","and","I","will","grow","beard.a","fill.ed","with","riddle.s","and","it","will","flow","and","grow","like","waterfall.a","grows","from","glacier.a","that","melts","like","it", "is","2019"],
             ["hello", "dear", "musician"],
             ["feed","me","weird","stuff"],
             ["I", "whish", "I", "have.ed", "duck", "feet"],
             ["word.s.capitalize", "come.ed", "easy"],
             ["Emancipate", "yourselve.s", "from", "mental", "slavery", "None", "but",  "ourselve.s", "can",  "free",  "our" , "minds"]
            ]


