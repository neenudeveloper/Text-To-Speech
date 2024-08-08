from gtts import gTTS
import os

abc =open('sample.txt')
text =abc.read()
language = 'en'
obj = gTTS(text=text, lang=language,slow=False)

obj.save("Sample.mp3")


os.system("sample.mp3")

