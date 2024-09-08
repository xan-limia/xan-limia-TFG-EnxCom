import speech_recognition as sr
import os, sounddevice, config, time

class Recorder():
    def __init__(self):
        self.r = sr.Recognizer()
        self.filename = None

    def listen_forever(self):
        with sr.Microphone() as source:
            self.filename = "./wakeup/wakeup.wav"
            self.r.adjust_for_ambient_noise(source=source)
            os.system("echo Escuchando...")
            audio = self.r.listen(source=source, phrase_time_limit=config.RECORD_MAX_TIME)

            a = open(self.filename, "wb")
            a.write(audio.get_wav_data())
            a.close()
        try:
            latency1 = time.time()
            # Ejecucion del modelo de Vosk
            os.system("vosk-transcriber -m /home/xan-limia/vosk/vosk-model-small-es-0.42 -l es -i ./wakeup/wakeup.wav -o ./wakeup/wakeup.txt")
            latency2 = time.time()
            print(f"Tiempo vosk: {latency2-latency1}")
            # Recuperacion de la respuesta
            with open('./wakeup/wakeup.txt') as file:
                output  = file.read()
            
        except:
            output = ""

        finally:
            return output

    def record_audio(self, record_max_time = config.RECORD_MAX_TIME):
        # Configuracion del microfono
        with sr.Microphone() as source:
            # Fichero donde se va a guardar
            self.filename = "./audio/audio.wav"
            # Ajuste del ruido ambiente
            self.r.adjust_for_ambient_noise(source=source)
            os.system("echo Escuchando...")
            # Escucha durante x segundos, si el usuario termina antes la gravacion tambien
            audio = self.r.listen(source=source, phrase_time_limit=record_max_time)

            # Escritura del audio en el fichero
            a = open(self.filename, "wb")
            a.write(audio.get_wav_data())
            a.close()

    def default_audio(self):
        self.filename = config.DEFAULT_AUDIO_NAME        
