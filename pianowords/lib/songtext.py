import tracery
from assoc import *
import random
from tracery.modifiers import base_english
import datetime
from weatherstuff import getweather 
import filestuff

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






absurdrules = {
    'origin': '#hello.capitalize#, #location#!',
    'hello': ['hello', 'greetings', 'howdy', 'hey'],
    'location': ['world', 'solar system', 'galaxy', 'universe']
}

repetetiverules = {
    'origin': '#hello.capitalize#, #location#!',
    'hello': ['hello', 'greetings', 'howdy', 'hey'],
    'location': ['world', 'solar system', 'galaxy', 'universe']
}




def updateobject(obj, objtype):
    global confirmedwordlist
    #get assocs
    fetchandstorewords(obj, confirmedwordlist)
    print(obj)
    newobj = {}
    for w in obj:
        newobj = newobj + getTypeFromAssoc(w,objtype)
    print (newobj)

    

loadObjectsFromDisk()

gletcher = {
    'melting' : '#feed.capitalize# me #weird# #music#',
    'feed': feed,
    'sentence' :["feed","me","weird","music","and","I","will","grow","a","beard","filled","with","riddles","and","it","will","flow","and","grow","like","a","waterfall","grows","from","a","glacier","that","melts","like","it's","2018"]
}

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
    print("printing new sentence")
    print (newsentence)
    return newsentence


def convertSentenceToTraceobj(tracename, sentence, traceobj):
    trace = ""
    for idx, word in enumerate(sentence):
        #split modifiers
        mods = None
        if "." in word:
            mods = word.split(".")[1:len(word.split("."))]
            print(mods)
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
                print (mods)
                for mod in mods:
                    word = word + "." + mod
            word = "#" +  word + "#"
        trace = trace + word + " "
    traceobj[tracename] = [trace]
    print (traceobj)
    return traceobj 

def makeSense(traceobj,tracename):
    grammar = tracery.Grammar(traceobj)
    grammar.add_modifiers(base_english)
    print(grammar.flatten("#"+tracename+"#"))  

#gletcherobjects


sentence = ["feed","me","weird","music","and","I","will","grow","a","beard","filled","with","riddles","and","it","will","flow","and","grow","like","a","waterfall","grows","from","a","glacier","that","melts","like","it's","2018"]
sentence = ["hello", "dear", "musician"]
sentence = ["feed","me","weird","stuff"]
sentence = ["I", "whish", "I", "had", "duck", "feet"]
sentence = ["word.s.capitalize", "come.ed", "easy"]
