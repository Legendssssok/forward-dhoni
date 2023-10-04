import requests
import time
import telebot

bot = telebot.TeleBot("6339536087:AAF8Q0riD04DxpLSFf4mn-J4QaVpvL9iiTc")
DHONIPRIME_URL = 'https://dhoniprime.firebaseio.com/Match.json'


def get_urls() -> list[str]:
    r = requests.get(url=DHONIPRIME_URL).json()
    link = []
    for k, v in r.items():
        # links = v['posttitle' + "\nBe Active ;)"] + ' -> '
        links = "https://t.me/DhOniFantasyPrimeLeaKs "
        links += v['matchLink'] if v.get(
            'matchLink') is not None else v['posttitle'] + "\nBe Active ;)"
        links += " @DhOniFantasyPrimeLeaKs"
        links += "\n\n➡️ DhOni FinaL \n\n➡️ Join Channel : @DhOniFantasyPrimeLeaKs\n➡️ T.me/DhOniFantasyPrimeLeaKs"
        link.append(links)

    return links


global text
text = get_urls()
# bot.send_message(chat_id='-1001481256781',
#                          text=text, disable_web_page_preview=True)


@bot.message_handler(commands=['refresh'])
def send_welcome(message):
    bot.reply_to(message, get_urls())


while (True):
    text_new = get_urls()
    if text_new != text:
        bot.send_message(chat_id='-1001481256781',
                         text=text_new, disable_web_page_preview=True)
        print("Links uploaded! Sent to channel")
        text = text_new
    time.sleep(0.1)

bot.infinity_polling()
