from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import smtplib




bot = ChatBot('Test')

bot.set_trainer(ListTrainer)



def talkToMe(audio):
     print(audio)
     tts = gTTS(text=audio, lang='en')
     tts.save('audio.mp3')
     os.system('mpg123 audio.mp3')

def myCommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        talkToMe('Hello')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        talkToMe('Your last command could not be heard')
        command = myCommand()

    return command



for files in os.listdir('C:/Users/Prithvik\Data/'):
    data = open('C:/Users/Prithvik\Data/' + files,'r').readlines()
    bot.train(data)

while True:
    message = myCommand()
    if message != 'bye':
        response = bot.get_response(message)
        talkToMe('%s'%response)
    if message == 'bye':
        talkToMe('Bye. Have a nice day')
        break






