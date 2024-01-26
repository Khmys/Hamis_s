from pyrogram import Client, filters

api_id = 979271
api_hash = "ba5c79822456d986a855b1bb1e4aafaf"
bot_token = "6555046105:AAGtZO-OAmrDPYxXz4zxKuINvyWdGZQEbeY"

app = Client(
    "Msimbo",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command('start'))
def start(bot, msg):
    app.send_message(msg.chat.id, text="sawa")



@app.on_message(filters.private)
async def copy_message(client, message):
    chat_ID = message.chat.id
    await app.copy_message(
                    chat_id=chat_ID,
                    from_chat_id=chat_ID,
                    message_id=message.id
                )

print('Tayari...')
app.run()
