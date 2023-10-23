import requests
import time
import telebot

print("Server is Running")


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

def get_url() -> list[str]:
    r = requests.get(url=DHONIPRIME_URL).json()
    link = []
    for k, v in r.items():
      links = v['matchLink'] if v.get(
            'matchLink') is not None else "Team Coming"
      link.append(links)
      
      return links


global text
text = get_urls()
texts = get_url()
# bot.send_message(chat_id='-1001481256781',
#                          text=text, disable_web_page_preview=True)
# bot.send_message(chat_id='-1001950168101',
#                          text=texts, disable_web_page_preview=True)



@bot.message_handler(commands=['refresh'])
def send_welcome(message):
    bot.reply_to(message, "i am working")


while (True):
    text_new = get_urls()
    text_news = get_url()
    if text_new != text:
        bot.send_message(chat_id='-1001481256781',
                         text=text_new, disable_web_page_preview=True)
        bot.send_message(chat_id='-1001950168101',
                         text=text_news, disable_web_page_preview=True)
        print("Links uploaded! Sent to channel")
        text = text_new
    time.sleep(0.1)

bot.infinity_polling()
