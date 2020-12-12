from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Test')

bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Prithvik\Data/'):
    data = open('C:/Users/Prithvik\Data/' + files,'r').readlines()
    bot.train(data)

while True:
    message = input('You: ')
    if message.strip() != 'bye':
        response = bot.get_response(message)
        print('Bot: ',response)
    if message.strip() == 'bye':
        print('Bot: Bye. Have a nice day')
        break
