   
#importing speech_recognition module
import speech_recognition as sr

#importing webbrowser module which allows displaying web based documents to users
import webbrowser


#setting up the microphone
sr.Microphone(device_index=1)


#recognises speech input from microphone
r=sr.Recognizer()


#setting ambient noise levels
r.energy_threshold=5000


#use default microphone as audio source for listening
with sr.Microphone() as source:

    print("Speak!")

    audio=r.listen(source)

    try:

        text=r.recognize_google(audio) #using google API to recognise audio

        print("You said : {}".format(text))

        url='https://www.google.co.in/search?q=' #the default search url

        search_url=url+text

        webbrowser.open(search_url) #opens the required url in the webbrowser

    except:

        print("Can't recognize")
