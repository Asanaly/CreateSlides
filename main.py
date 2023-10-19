import speech_recognition as sr
import openai
import time


from Google_Search import *

OPENAI_API_KEY = "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"
FirstTimeRunning = True

#Get the audio from microphone
r = sr.Recognizer()


def RequestFromGPTShortTitle(message):
    prompt = str("""
    You are helping me with a summarizing text
    Give a two main keywords for this speech inside []. 
    Then give a short title within 4 words inside {}. 
    Don't write anything else except for answer.
    
    """ + message)

    openai.api_key = OPENAI_API_KEY

    # Construct the message object
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256
    )

    return response.choices[0].message['content']



    #The active listener function and download image with name
def ListeningLoop(name):
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout=3)
            print("DONE")
    except:

        print("Trying again")
    try:
        print("Summarizing text")
        RecognizedAudio = r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
        Keypoints = str(RequestFromGPTShortTitle(RecognizedAudio))
        print("Here are keypoints", Keypoints)
        print("Only keypoints: ", GetSubString("[", "]" , Keypoints))
        print("Only title: ", GetSubString("{", "}" , Keypoints))
        print("What is requested: " , Keypoints)
    except sr.RequestError as e:
        print("Could not request results from Whisper API")
    try:
            #Downloaded image with speech title
        DownloadImage(str(Keypoints), name)
            #DownloadImage(str(GetSubString("[", "]" , Keypoints)).split(",")[0] + str(GetSubString("(", ")" , Keypoints)), "Title1")
    except:
        print("Problems!")

    return GetSubString("{", "}" , Keypoints)