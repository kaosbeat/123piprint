from subprocess import call
import pickle
import os


def object2File(obj, filename):
	f=open(filename.encode('utf-8'), 'wb')
	# f=open(filename.decode("ascii", "ignore"), 'wb')
	pickle.dump(obj, f)
	f.close()

def file2Object(filename):
	f=open(filename.encode('utf-8'), 'rb')
	# f=open(filename.decode("ascii", "ignore"), 'wb')
	obj = pickle.load(f)
	return obj

def checkIfExists(file):
	os.path.isfile(file.encode('utf-8'))
	# os.path.isfile(file.decode("ascii", "ignore"), 'wb')

def convertAndTrace(infile, tempfile, outsvg):
	# infile = "arrow.jpg"
	# outbmp = "temp.bmp"
	# # outsvg = "out.svg"
	call(["convert", "-alpha", "remove", infile.encode('utf-8'), tempfile.encode('utf-8')]) 
	call(["potrace", "-s", tempfile.encode('utf-8') , "-o", outsvg.encode('utf-8')])
	# print tempfile
	print (infile.decode("ascii", "ignore"))
	print (outsvg.decode("ascii", "ignore"))
	# call(["convert", "-alpha", "remove", infile.decode("ascii", "ignore"), tempfile]) 
	# call(["potrace", "-s", tempfile, "-o", outsvg.decode("ascii", "ignore")])


def loadObjectsDirectory2wordlist(directory,wordlist):
	for filename in os.listdir(directory):
		if filename.endswith(".assoc"):
			word = (filename[0:-6])
			wordlist.append(word)
			# f = open(filename, 'r')
			# text = f.read()
			continue
		else:
			continue