from src.heart.heartSistem import *

def onGetMultiProccessingVoz(text):
        proceso = multiprocessing.Process(target=onGetVoz, args=(text,))
        proceso.start()
        proceso.join()
        

def onGetVoz(text):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-70)
        textVoz = text
        engine.say(textVoz)
        engine.runAndWait()