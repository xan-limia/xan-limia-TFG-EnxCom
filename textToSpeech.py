from gtts import gTTS
import config as conf
import os

def text_to_speech(text):
    # Generacion del audio
    tts = gTTS(text=text, lang=conf.LANGUAGE)
    tts.save('./audio/file.mp3')
    # Reproduccion del audio por el altavoz por defecto
    os.system("mpg123 ./audio/file.mp3")
    os.remove('./audio/file.mp3')
