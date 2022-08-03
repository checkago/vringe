import telebot
import requests
import time
from bs4 import BeautifulSoup
a = [0]
API_TOKEN = '5505028871:AAEcx8dnqxvH83YqIPczOa2j9xjdWJ0hWMg'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler()
def pars(message):
    while True:
        url = requests.get('https://vringe.com')
        soup = BeautifulSoup(url.text, 'html.parser')
        cod1 = soup.find_all('div', class_='time')
        cod2 = soup.find_all('div', class_='title')
        cod3 = cod1[0].text
        cod4 = cod2[6].text

        if cod3 not in a:
            print(cod3)
            a.append(cod3)
            a.pop(0)
            bot.send_message(message.chat.id, cod3)
            bot.send_message(message.chat.id, cod4)
        time.sleep(300)


bot.polling(none_stop=True)
