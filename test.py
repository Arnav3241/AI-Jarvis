from speech_recognition import Recognizer, Microphone


#A Function For Speech Recognition:
# def SR():
#     recognition = Recognizer()
#     with Microphone() as source:
        
#         print(f"Jarvis: Listening...")
#         recognition.pause_threshold = 1
#         Audio = recognition.listen(source, 0, 4)
        

#     try:
#         print(f"Jarvis: Recognizing...")
#         query = recognition.recognize_google(Audio, language="en-in")
#         print(f"Your Command: {query}\n")

#     except:
#         return ""

#     return query

#A Function For Speech Recognition:
def SR():
    recognition = Recognizer()
    with Microphone() as source:
        recognition.adjust_for_ambient_noise(source)
        print(f"Jarvis: Listening...")
        recognition.pause_threshold = 1
        Audio = recognition.listen(source, 0, 4, )
        

        try:
            print(f"Jarvis: Recognizing...")
            query = recognition.recognize_google(Audio, language="en-in")
            print(f"Your Command: {query}\n")

        except:
            print("")
            return ""

    return query
    
while True: 
    SR()