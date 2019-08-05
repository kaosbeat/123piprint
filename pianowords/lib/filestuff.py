from subprocess import call
from slugify import slugify
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

def cleanFilename(filename):
	#https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
	# filename = 'Very / Unsafe / file\nname hähä \n\r .txt'
	clean_basename = slugify(os.path.splitext(filename)[0])
	clean_extension = slugify(os.path.splitext(filename)[1][1:])
	if clean_extension:
		clean_filename = '{}.{}'.format(clean_basename, clean_extension)
	elif clean_basename:
		clean_filename = clean_basename
	else:
		clean_filename = 'none' # only unclean characters
	return clean_filename

def txt2file(txt, filename):
	import songtext
	f=open(filename.encode('utf-8'), 'w+')
	for line in songtext.currentprint:
		f.write(line)
	f.close()
