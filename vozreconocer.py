import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Habla al microfono ")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Dijiste esto: {}".format(text))
    except:
        print("Lo siento, no te pude entender")
    
    
