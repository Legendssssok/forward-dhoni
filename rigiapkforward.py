import threading
import time

import requests
import telebot

bot = telebot.TeleBot("7142884055:AAGjCBNF9e407U8PW0sr3du0fhI1uGL1NYk")
target_channel = -1002069704830
forward_images = False  # Variable to track if image forwarding is on or off

print("Server is Running")


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    global target_channel, forward_images

    if str(message.from_user.id).startswith("5252650067"):
        if message.text.startswith("/set_channel"):
            try:
                target_channel = "-100" + str(
                    message.text.split()[1]
                )  # Extract channel ID from the message
                bot.reply_to(
                    message, f"Target channel has been set to {target_channel}."
                )
                bot.reply_to(
                    message,
                    f"Must Add The Bot To Target Channel. If You Didn't Add Forwarding Will Not Work.",
                )
            except IndexError:
                bot.reply_to(message, "Please provide a valid channel ID.")

        elif message.text.startswith("/start"):
            command_list = [
                "/set_channel - Set the target channel for forwarding messages.",
                "\n/toggle_images - Toggle image forwarding on or off.",
                "\n/settings - To Check Current Setting",
                "\n/reset - Reset Settings to default.",
            ]

            # Concatenate the command list into a single string
            command_text = "\n".join(command_list)

            # Welcome message
            welcome_message = "Welcome to the bot! Here are the available commands:\n\n"

            # Send the welcome message and the command list to the user
            bot.reply_to(message, f"{welcome_message}{command_text}")

        elif message.text.startswith("/toggle_images"):
            forward_images = not forward_images  # Toggle the value
            if forward_images:
                bot.reply_to(message, "Image forwarding is now ON.")
            else:
                bot.reply_to(message, "Image forwarding is now OFF.")

        elif message.text.startswith("/settings"):
            bot.reply_to(
                message,
                f"Target channel: {target_channel}\nImage forwarding: {'ON' if forward_images else 'OFF'}",
            )

        elif message.text.startswith("/reset"):
            # Reset target channel to default
            target_channel = -1002069704830
            forward_images = False
            bot.reply_to(message, "Settings has been reset to default.")

        else:
            # If the user issued an invalid command, send a message informing them
            bot.reply_to(
                message, "Invalid command. Please use one of the available commands."
            )

    else:
        # If the user is not authorized, send a warning message
        bot.reply_to(message, "You are not authorized to use this bot.")
        bot.reply_to(message, "Contact : @Atw786Leaker.")


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


def get_urls():
    global text, image
    while True:
        try:
            response, response2 = fetch_urls()
            if response != text and response.strip():  # Check if response is not empty
                print(response)
                bot.send_message(target_channel, response)
                text = response

            if forward_images and response2 and response2 != image:
                print(response2)
                bot.send_photo(target_channel, response2)
                image = response2

            time.sleep(0.1)
        except Exception as e:
            print("Error:", e)


def fetch_urls() -> tuple:
    try:
        response = requests.post(url, headers=headers, params=params, json=data).json()[
            "channels"
        ][0]["messages"][-1]["text"]
    except:
        response = ""
    try:
        response2 = requests.post(
            url, headers=headers, params=params, json=data
        ).json()["channels"][0]["messages"][-1]["attachments"][0]["image_url"]
    except:
        response2 = None

    return response, response2


text = ""
image = ""

# Start the loop in a separate thread
thread = threading.Thread(target=get_urls)
thread.start()

# Start the bot
bot.polling()
