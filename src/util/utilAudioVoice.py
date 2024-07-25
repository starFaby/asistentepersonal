from src.heart.heartSistem import *

def onGetMultiProccessingAudioVoz(text):
        proceso = multiprocessing.Process(target=onGetAudioVoz, args=(text,))
        proceso.start()
        proceso.join()
        

def onGetAudioVoz(text):
        tts = gTTS(text=text, lang='es')
        filename = 'src/util/voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)