import requests
import time
import telebot

print("Server is Running")
bot = telebot.TeleBot("6339536087:AAF8uq2jysqeHe3A82gWng85zBFgNhdK53I")
DHONIPRIME_URL = 'https://dhoniprime.firebaseio.com/Match.json'


def get_urls() -> list[str]:
    r = requests.get(url=DHONIPRIME_URL).json()
    links = ""
    for k, v in r.items():
        # links = v['posttitle' + "\nBe Active ;)"] + ' -> '
        links = "https://t.me/DhOniFantasyPrimeLeaKs "
        links += v['matchLink'] if v.get(
            'matchLink') is not None else v['posttitle'] + "\nBe Active ;)"
        links += " @DhOniFantasyPrimeLeaKs"
        links += "\n\n➡️ DhOni FinaL \n\n➡️ Join Channel : @DhOniFantasyPrimeLeaKs\n➡️ T.me/DhOniFantasyPrimeLeaKs"
    return links


def get_url() -> list[str]:
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
    if text_new == text:
        bot.send_message(chat_id='-1001481256781',
                         text=text_new, disable_web_page_preview=True)
        bot.send_message(chat_id='-1001950168101',
                         text=text_news, disable_web_page_preview=True)
        print("DhOni Links uploaded! Sent to channel")
        text = text_new
    time.sleep(0.1)


bot.infinity_polling()
