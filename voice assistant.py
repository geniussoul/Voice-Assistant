import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os



def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as  source:
        print('...Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print('...Recognizing....')
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('....not understanding....')

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say(x)
    engine.runAndWait()
speechtx('hello genius')


if __name__=='__main__':
    # if sptext().lower()=='hey jarvis'
    while True:
        data1 = sptext().lower()
        if 'your name' in data1:
            name = 'my name is jarvis'
            speechtx(name)

        elif 'old are you' in data1:
            age = 'i donot have any age i am created by genius scholar '
            speechtx(age)

        elif ' time' in data1:
            time = datetime.datetime.now().strftime('%I%M%p')
            speechtx(time)

        elif 'youtube' in data1:
            webbrowser.open('https://www.youtube.com/')

        elif 'joke' in data1:
            joke_1 = pyjokes.get_joke(language='en', category='neutral')
            print(joke_1)

        elif 'music' in data1:
            add = 'D:/songs'
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add, listsong[-1]))

        elif 'exit' in data1:
            speechtx('---thank you---')
            break
            time.sleep(30)





        # else:
        #     print('---thank you---')







