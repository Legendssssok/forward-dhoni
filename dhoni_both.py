import requests
import time
import telebot

print("Server is Running")
bot = telebot.TeleBot("6339536087:AAF_SMbdKV0Pku9lioxG2FWagPCYW83jGFU")
DHONIPRIME_URL = 'https://dhonifantasysports-1b42c-default-rtdb.firebaseio.com/Match.json'


def get_urls() -> str:
    r = requests.get(url=DHONIPRIME_URL).json()
    links = ""
    for k, v in r.items():
        links = v['matchLink'] + " @DhOniFantasyPrimeLeaKs\n\n➡️ DhOni FinaL \n\n➡️ Join Channel : @DhOniFantasyPrimeLeaKs\n➡️ T.me/DhOniFantasyPrimeLeaKs" if v.get(
            'matchLink') is not None else v['posttitle'] + " join\n\nBe Active ;)"
    return links


def get_url() -> str:
    r = requests.get(url=DHONIPRIME_URL).json()
    links = ""
    for k, v in r.items():
        links = v['matchLink'] if v.get(
            'matchLink') is not None else "Team Coming"
    return links


global text
text = get_urls()
texts = get_url()

while (True):
    text_new = get_urls()
    text_news = get_url()
    if text_new != text:
        bot.send_message(chat_id='-1001481256781',
                         text=text_new, disable_web_page_preview=True)
        bot.send_message(chat_id='-1001950168101',
                         text=text_news, disable_web_page_preview=True)
        print("DhOni Links uploaded! Sent to channel")
        text = text_new
    time.sleep(0.1)


bot.infinity_polling()
