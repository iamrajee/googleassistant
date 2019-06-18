from gtts import gTTS
import os
import sys
import time
from time import *

input = sys.argv[1]
path = '/home/pi/googleassistant/mp3/'
tokenlist = input.split(' ')
#print("tokenlist => ",tokenlist)


def justsave(input):
        inputstrip = "".join(input.split(' '))
        path = '/home/pi/googleassistant/mp3/'
        filename = path + inputstrip + '.mp3'
        tts = gTTS(text=input, lang='hi')
        tts.save(filename)

def saveij(i,j):
        print('saveing for =>'+" ".join(tokenlist[i:j+1]))
	justsave(" ".join(tokenlist[i:j+1]))

def breakinput(input):
	filelist = os.listdir(path)
	#tokenlist = input.split(' ')
	#print("tokenlist => ",tokenlist)
	i = 0
	savedlist = []
	while (i < len( tokenlist)):
		token = tokenlist[i]
		print(token)
		flag = 0
		max_j = 0
		for file in filelist:
			file2 = file.split(".mp3")[0]
			if token in file2:
				flag=1
				if i < len(tokenlist)-1:
					print(i,len(tokenlist))
					for j in range(i+1,len(tokenlist)):
						print("j:",j)
						if tokenlist[j] in file2:
							token+=tokenlist[j]
						else:
							if token == file2:
								savedlist.append(token)
								i=j
								max_j=0
								break
							else:
								#print(token,file2)
								#saveij(i,j-1)
								max_j = max(max_j,j)
								break
					if max_j == 0:
						break
				else:
					savedlist.append(token)
					i+=1
					break
		if max_j != 0:
        		saveij(i,max_j-1)
	                savedlist.append(token)
        	        i=max_j
		if flag == 0:
			saveij(i,i)
			savedlist.append(token)
			i+=1
	return savedlist

def playlist(mp3list):
	for ele in mp3list:
		elepath = path+ele+".mp3"
		os.system("mpg123 "+elepath)

def simplesaveplay(input):
	inputstrip = "".join(input.split(' '))
	filename = path + inputstrip + '.mp3'
	print("input : " + input + ", filename : " + filename)
	if os.path.isfile(filename):
		        os.system("mpg123 "+filename)
	else:
		tts = gTTS(text=input, lang='hi')
		tts.save(filename)
		os.system("mpg123 "+filename)

start = time()
savedlist = breakinput(input)
print("savedlist=>",savedlist)
playlist(savedlist)
#simplesaveplay(input)
print("\n\n****** CPU_TIME : " + str(time()-start) + " Sec *************")
