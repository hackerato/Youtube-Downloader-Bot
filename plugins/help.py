from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Поддерживает только Youtube Single (без плейлиста). Просто отправьте ссылку на Youtube"
    await message.reply_text(helptxt)
