import requests, time
import telebot

bot = telebot.TeleBot("6339536087:AAF8Q0riD04DxpLSFf4mn-J4QaVpvL9iiTc")
DHONIPRIME_URL = 'https://dhoniprime.firebaseio.com/Match.json'

def get_urls() -> list[str]:
	r = requests.get(url=DHONIPRIME_URL).json()
	link = []
	for k, v in r.items():
		# links = v['posttitle'] + ' -> ' 
		links = v['matchLink'] if v.get('matchLink') is not None else 'Be Active ;)'
		links += '\n''\n'
		links += "DhOni FinaL" 
		links += '\n''\n'
		links += "Join Channel"  
		links += '\n'  
		links += "https://t.me/DhOniFantasyPrimeLeaKs"  
		link.append(links)


	return links

global text

text = get_urls()
bot.send_message(chat_id='-1001481256781', text=text)

@bot.message_handler(commands=['refresh'])
def send_welcome(message):
	bot.reply_to(message, get_urls())

while (True):
	text_new = get_urls()
	if text_new != text:
		bot.send_message(chat_id='-1001481256781', text=text_new)
		print("Links uploaded! Sent to channel")
		text = text_new
	time.sleep(0.1)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am DhoniBot.
I post all the latest Dream11 links. Use /refresh to use me.\
""")

bot.infinity_polling()
