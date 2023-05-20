
from gtts import gTTS
t=open("text",'r')

s= gTTS(t.read())

s.save('result_audio.mp3')
