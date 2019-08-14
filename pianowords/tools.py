import sys
sys.path.append('lib')
import filestuff
from unidecode import unidecode


def remove_non_ascii(text):
    return unidecode(str(text))


songs = filestuff.file2Object("songs.store")
hashtags = ["123piano", "inspiration"]
# for item in songs:
#     for word in songs[item]["text"]:
#         if word not in hashtags:
#             print(word.encode("utf-8"))



def cleanSongs(hashtags):
    resong = []
    for item in songs:
        for word in songs[item]["text"]:
            #clean unwanted words/hashtags, make the pure ascii in one go
            if word not in hashtags:
                resong.append(remove_non_ascii(word))
            else:
                print("found and removed hashtag " + word)

        songs[item]["text"] = resong
    
    for item in songs:
        for word in songs[item]["text"]:
             print(word.encode("utf-8"))
    filestuff.object2File(songs, "songs.store")


cleanSongs(["123piano", "inspiration"])