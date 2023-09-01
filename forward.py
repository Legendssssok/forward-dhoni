from pyrogram import Client, filters
from pyrogram.types import Message
import os
from pyrogram.types import InputMediaPhoto


API_ID = 11573285
API_HASH = "f2cc3fdc32197c8fbaae9d0bf69d2033"
BOT_TOKEN = "6628233864:AAGIlIOZDqEp0VaL4DF47wE40A18fJUjiQY"


app = Client("editor", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)

source_id = -1001879320894
target_id = -1001608380232
photo_id = {}
text_id = {}


@app.on_message(filters.chat(target_id))
def dump_message(client, message):
    if message.text:
        text_id["last_message"] = message.id
    elif message.photo:
        photo_id["last_message"] = message.id


@app.on_message(filters.command(["start", "help"]))
def welcome_message(client, message):
    app.send_message(message.chat.id, """\
Hi there, I am editorBot.
I edit all the latest message. Use /start to use me.
\
""")


@app.on_message(filters.chat(source_id))
def forward_to_target_channel(client, message):
    msg = app.send_message(target_id, "Team Coming ")
    current_id = msg.id
    last_message = current_id
    if last_message:
        if message.text:
            try:
                app.edit_message_text(
                    chat_id=target_id, message_id=last_message, text=message.text)
            except:
                new_message = text_id.get("last_message")
                app.edit_message_text(
                    chat_id=target_id, message_id=new_message, text=message.text)
        if message.photo:
            file_id = client.download_media(message)
            try:
                app.edit_message_media(
                    chat_id=target_id, message_id=last_message, media=InputMediaPhoto(file_id))
            except:
                new_message = photo_id.get("last_message")
                app.edit_message_media(
                    chat_id=target_id, message_id=new_message, media=InputMediaPhoto(file_id))
            os.remove(file_id)
        app.send_message(target_id, "Team Updated")

            
    else:
        app.send_message(target_id, message.text)


print("Server is Running")
app.run()
