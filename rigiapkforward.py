import requests
import telebot

king = telebot.TeleBot("7142884055:AAHl9bnl5-fstLJDcl8OvKoQcO8w3eCCMZA")
target_channel = -1002069704830
forward_images = False

print("Server is Running")


@bot.message_handler(commands["start"])
async def handle_start(message):
    if str(message.from_user.id).startswith("5252650067"):
        command_list = [
            "/set_channel - Set the target channel for forwarding messages.",
            "\n/toggle_images - Toggle image forwarding on or off.",
            "\n/settings - To Check Current Setting",
            "\n/reset - Reset Settings to default.",
        ]
        command_text = "\n".join(command_list)
        welcome_message = "Welcome to the bot! Here are the available commands:\n\n"
        bot.reply_to(message, f"{welcome_message}{command_text}")


@bot.message_handler(commands["set_channel"])
async def set_channel(message):
    global target_channel, forward_images
    if str(message.from_user.id).startswith("5252650067"):
        try:
            target_channel = int(
                message.text.split()[1]
            )  # Extract channel ID from the message
            bot.reply_to(message, f"Target channel has been set to {target_channel}.")
            bot.reply_to(
                message,
                f"Must Add The Bot To Target Channel. If You Didn't Add Forwarding Will Not Work.",
            )
        except IndexError:
            bot.reply_to(message, "Please provide a valid channel ID.")


@bot.message_handler(commands["toggle_images"])
async def toggle_images(message):
    global target_channel, forward_images
    if str(message.from_user.id).startswith("5252650067"):
        try:
            forward_images = not forward_images  # Toggle the value
            if forward_images:
                bot.reply_to(message, "Image forwarding is now ON.")
            else:
                bot.reply_to(message, "Image forwarding is now OFF.")
        except Exception as e:
            print(e)


url = "https://chat.stream-io-api.com/channels"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjI2YTQ4ODk1OGIwZjAyMTAxOTdjYzJkIn0.oYUM8eJqbR0LU6G-mcEt_eCKI_vU5Yu7I6RYbXvXhRI",
    "stream-auth-type": "jwt",
    "X-Stream-Client": "stream-chat-javascript-client-browser-6.9.0",
    "x-client-request-id": "d413bb4f-fd28-44ef-ad7e-c4f739c868ec",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    "Referer": "https://rpy.club/chat",
}

data = {
    "filter_conditions": {
        "members": {"$in": ["626a488958b0f0210197cc2d"]},
        "type": {
            "$in": ["BroadcastChannelPaid", "GroupsPaid", "Groups", "BroadcastChannel"]
        },
        "support_group": {"$nin": [True]},
    },
    "sort": [],
    "state": True,
    "watch": True,
    "presence": False,
}

params = {
    "user_id": "626a488958b0f0210197cc2d",
    "connection_id": "65e9ec5e-0a09-243b-0000-00000092a206",
    "api_key": "y5w6ct63tj2y",
}


def get_urls() -> list[str]:
    try:
        response = requests.post(url, headers=headers, params=params, json=data).json()[
            "channels"
        ][0]["messages"][-1]["text"]
    except:
        response = text
    try:
        response2 = requests.post(
            url, headers=headers, params=params, json=data
        ).json()["channels"][0]["messages"][-1]["attachments"][0]["image_url"]
    except:
        response2 = image

    return response, response2


global text, image

text = ""
image = ""

while True:
    response, response2 = get_urls()
    if response != text:
        print(response)
        king.send_message(target_channel, response)
        text = response

    if response2 != image:
        print(response2)
        king.send_photo(target_channel, response2)
        image = response2

king.infinity_polling()
