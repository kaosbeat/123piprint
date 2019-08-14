import sys
sys.path.append('lib')
import filestuff
songs = filestuff.file2Object("songs.store")
hashtags = ["123piano", "inspiration"]
for item in songs:
    for word in songs[item]["text"]:
        if word not in hashtags:
            print(word.encode("utf-8"))



def cleanSongs(hashtags):
    resong = []
    for item in songs:
        for word in songs[item]["text"]:
            if word not in hashtags:
                resong.append(word)
            else:
                print("found and removed hashtag " + word)
        songs[item]["text"] = resong
    # for item in songs:
    #     for word in songs[item]["text"]:
    #          print(word.encode("utf-8"))
    filestuff.object2File(songs, "songs.store")


# cleanSongs(["123piano", "inspiration"])