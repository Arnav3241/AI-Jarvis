from speech_recognition import Recognizer, Microphone
from Chatbot.NLTK_Utils import Tokenize, bagOfWords
from Chatbot.NeuralNet import NeuralNet
from Main.RemoveFile import RemoveFile
from Chatbot.Training import Training
from Main.LoadJson import loadJson
from functions import *
import threading
import pyfirmata
import datetime
import pyttsx3
import random
import torch

# Made By Arnav Singh

#Important Variables:
EmailAddress = "arnav.singh.legendary.202@gmail.com"        #The E-Mail Address required for checking & sending email
Device = torch.device("cpu")                                #The Device We Are Using To Train The Neural Network
numEchos = 1000                                             #Number of Echos To Train The Model
batchSize = 8                                               #Number Of Training Examples Utilized In One Iteration
LR = 0.001                                                  #The Rate At Which The Model Sould Learn
hiddenLayer = 8                                             #The Size Of The Hidden layer
PthFilePath = "Database\Chatbot\Chatbot.pth"                #The Path Of the PTH File Saved During The Training Function
Task = ""                                                   #The Task Of The Intents Of the output from the Neural Network
CTH = datetime.datetime.now().strftime("%H")
CTM = datetime.datetime.now().strftime("%M")


#Changing JSON Data to Python Dictionary:
DataJSON = loadJson('Database\Basic\Data.json').data
IntentsJSON = loadJson('Database\Intents\intents.json').data


#A Function For Speech Recognition:
def SR():
    recognition = Recognizer()
    with Microphone() as source:
        print(f"{DataJSON['Data']['Assistant_Data']['Assistant_Name']}: Listening...")
        recognition.pause_threshold = DataJSON['Data']['STT_Data']['Pause_Threshold']
        Audio = recognition.listen(source, 0, 4, )

    try:
        print(f"{DataJSON['Data']['Assistant_Data']['Assistant_Name']}: Recognizing...")
        query = recognition.recognize_google(Audio, language="en-in")
        print(f"Your Command: {query}\n")

    except:
        return ""

    return query

#A Function For TTS:
def Speak(text): 
    print(f"{DataJSON['Data']['Assistant_Data']['Assistant_Name']}: {text}")
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty("rate", DataJSON['Data']['TTS_Data']['Speech_Rate'])

#A Function For Wishing Me According To The Time 
def Get_Time():
    Hour = int(datetime.datetime.now().hour)
    if Hour>=0 and Hour<=12:
        T = "Good Morning"
    elif Hour>12 and Hour<18:
        T = "Good afternoon"
    else:
        T = "Good evening"
    return T


# #Starting Lines & Arduino Connection:
# Speak("Initializing Jarvis")
# Speak("Starting All System Applications")
# Speak("Establishing Connections With The Arduino Board")
Arduino = pyfirmata.Arduino(str(DataJSON['Data']['Arduino_Data']['Com_Port']))
# Arduino.digital[3].write(1)
# Speak("Connection Established")


#Arduino Functions:
def turnOnLight(digitalPin):
    Arduino.digital[int(digitalPin)].write(1)
    
def turnOffLight(digitalPin):
    Arduino.digital[int(digitalPin)].write(0)

#Mapping Of The Functions:
Mapping = {
    'exit' : Exit,
    'lightOn' : turnOnLight,
    'lightOff' : turnOffLight
}

def Main():    
    # RemoveFile(PthFilePath)
    # Speak("Training The Model\n")
    # ChatBot = Training('Database\Intents\intents.json', ['!', ',', '.', '/', '?'], Device, numEchos, batchSize, LR, hiddenLayer, PthFilePath)
    # Speak(f"Training Complete With A Total Loss Of {ChatBot}")
    
    # Speak(f"{Get_Time}, Sir")
    # amPm = "pm" if int(CTH) > 12 else "am"
    # Speak(f"Currently it is {int(CTH) if int(CTH) < 13 else int(CTH)-12}:{CTM} {amPm}")
    # Speak("Online and ready sir!")

    #Loading The PTH File And Storing It In A Var named Data:
    Data = torch.load(PthFilePath)

    #Extracting Data From The PTH File:
    modelState = Data["model_state"]
    hiddenSize = Data["hidden_size"]
    outputSize = Data["output_size"]
    inputSize = Data["input_size"]
    allWords = Data["all_words"]
    Tags = Data["tags"]
    
    #Initialize The Chatbot:
    Model = NeuralNet(inputSize, hiddenSize, outputSize).to(Device)
    Model.load_state_dict(modelState)
    Model.eval()

    while True:
        try:
            Query = input()
            Pattern = Query
            Query = Tokenize(Query)
            X = bagOfWords(Query, allWords)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(Device)
            Output = Model(X)

            _, Predicted = torch.max(Output, dim = 1)
            tag = Tags[Predicted.item()]
            probs = torch.softmax(Output, dim = 1)
            prob = probs[0][Predicted.item()]

            if prob.item() > 0.75:
                for intent in IntentsJSON["intents"]:
                    if tag == intent["tag"]:
                        Reply = random.choice(intent["responces"])
                        Speak(f"{Reply}")
                        Task = intent["task"]
                        if Task !=  "":
                            if Task in Mapping.keys():
                                Mapping[Task]()
                            
        except Exception as exception:
           Speak(f"Opps, I Got a Exception: {str(exception)}")

        finally:
            print("")
        
            


#__name__ == "__main__" Loop That Allows The Main Function To Run In The Desired File
if __name__ == "__main__":
    mainThread = threading.Thread(target=Main, args=())      #Our Main Thread
    mainThread.start()                                       #Starting The Main Thread