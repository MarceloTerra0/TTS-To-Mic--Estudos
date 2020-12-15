#Huge thanks to https://stackoverflow.com/users/10021223/liambogur
#for providing this answer: https://stackoverflow.com/a/61674334

#requirements.txt
from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3

#native python
import time
import os
from math import ceil

#this is used for cleaning the temp file that we create
flag = 0
file_names = ["one.mp3", "two.mp3"]

while True:

    if flag == 0:
        flag = 1
    else:
        flag = 0

    #apparently this only works in pygame==2.0.0.dev8, 
    #since my 1.9.6 version gave me a lot of headaches
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    
    usr_text = input("Digite o texto que será falado: ")
    while not usr_text:
        usr_text = input("Digite o texto que será falado: ")
    

    tts = gTTS(text = usr_text, lang ="pt")
    #if lang is not provided, US English is the default one
    #tts = gTTS(text = usr_text)
    #sadly we need to save this to a file, instead of using it in memory
    #(at least I don't know how)
    tts.save(file_names[flag])

    mixer.music.load(file_names[flag])
    mixer.music.play()
    audio = MP3(file_names[flag])
    time.sleep(ceil(audio.info.length) + 0.3)
    mixer.stop()

    #this is needed so that there are no permission problems
    #since pygame is really finnicky with the mp3 files it opens
    if os.path.exists(os.path.abspath(file_names[abs(1-flag)])):
        os.remove(os.path.abspath(file_names[abs(1-flag)]))
