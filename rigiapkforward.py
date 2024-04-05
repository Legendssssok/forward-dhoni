import requests
import time
import telebot


king = telebot.TeleBot("6725785512:AAHjz2sARGFurhhjU8JMYcIPv2uc55I5aZg")

print("Server is Running")

url = 'https://chat.stream-io-api.com/channels'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjI2YTQ4ODk1OGIwZjAyMTAxOTdjYzJkIn0.oYUM8eJqbR0LU6G-mcEt_eCKI_vU5Yu7I6RYbXvXhRI',
    'stream-auth-type': 'jwt',
    'X-Stream-Client': 'stream-chat-javascript-client-browser-6.9.0',
    'x-client-request-id': 'd413bb4f-fd28-44ef-ad7e-c4f739c868ec',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://rpy.club/chat'
}

data = {
    "filter_conditions": {
        "members": {"$in": ["626a488958b0f0210197cc2d"]},
        "type": {"$in": ["BroadcastChannelPaid", "GroupsPaid", "Groups", "BroadcastChannel"]},
        "support_group": {"$nin": [True]}
    },
    "sort": [],
    "state": True,
    "watch": True,
    "presence": False
}

params = {
    'user_id': '626a488958b0f0210197cc2d',
    'connection_id': '65e9ec5e-0a09-243b-0000-00000092a206',
    'api_key': 'y5w6ct63tj2y'
}


def get_urls():
    try:
    	response = requests.post(url, headers=headers, params=params, json=data).json()["channels"][0]["messages"][-1]["text"]
    except:
    	response = text
    try:
    	response2 = requests.post(url, headers=headers, params=params, json=data).json()["channels"][0]["messages"][-1]["attachments"][0]["image_url"]
    except:
    	response2 = image
    
    return response, response2
    
    
global text, image
    
text = ""    
image = ""

while True:
	response, response2 = get_urls()
	if response != text:
		king.send_message(-1002053364776, response)
		text = response
		
	if response2 != image:
		king.send_photo(-1002053364776, response2)
		image = response2
	
king.infinity_polling()
