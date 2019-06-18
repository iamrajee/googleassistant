from gtts import gTTS
import os
import sys
import time
from time import *

input = sys.argv[1]
path = '/home/pi/googleassistant/mp3/'

def justsave(input):
        inputstrip = "".join(input.split(' '))
        filename = path + inputstrip + '.mp3'
        tts = gTTS(text=input, lang='hi')
        tts.save(filename)

def simplesaveplay(input):
	inputstrip = "".join(input.split(' '))
	filename = path + inputstrip + '.mp3'
	#print("input : " + input + ", filename : " + filename)
	if os.path.isfile(filename):
		        os.system("mpg123 "+filename)
	else:
		tts = gTTS(text=input, lang='hi')
		tts.save(filename)
		os.system("mpg123 "+filename)

start = time()
simplesaveplay(input)
print("\n\n****** CPU_TIME : " + str(time()-start) + " Sec *************")
