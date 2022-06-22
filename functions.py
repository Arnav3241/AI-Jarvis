from speech_recognition import Recognizer, Microphone
from Functions.Common import exitPrograme
from Main.LoadJson import loadJson
import pyttsx3

#Changing JSON Data to Python Dictionary:
DataJSON = loadJson('Database\Basic\Data.json').data
IntentsJSON = loadJson('Database\Intents\intents.json').data

def SR():
    recognition = Recognizer()
    with Microphone() as source:
        print(f"{DataJSON['Data']['Assistant_Data']['Assistant_Name']}: Listening...")
        recognition.pause_threshold = DataJSON['Data']['STT_Data']['Pause_Threshold']
        Audio = recognition.listen(source)

    try:
        print(f"{DataJSON['Data']['Assistant_Data']['Assistant_Name']}: Recognizing...")
        query = recognition.recognize_google(Audio, language="en-in")
        print(f"Your Command: {query}\n")

    except:
        return ""

    return query

def Speak(text): 
    print(f"{DataJSON['Data']['Assistant_Data']['Assistant_Name']}: {text}")
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty("rate", DataJSON['Data']['TTS_Data']['Speech_Rate'])

def Exit():
    exitPrograme()
    
