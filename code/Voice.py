from gtts import gTTS
import os
# takes in language and string to be turned into an mp3 file
def talk(text, lang):
    #converst string to mp3 using google TTS
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("code/voice.mp3")
    #runs mp3 file in system
    os.system("mpg123 -q " + "code/voice.mp3")
    return True
