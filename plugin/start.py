from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Канал", url="https://t.me/YouTubeDownloaderMaster")],
        [InlineKeyboardButton(
            "Сообщить об ошибке 😊", url="https://t.me/esumo")]
    ])
    welcomed = f"Привет <b>{message.from_user.first_name}</b>\n/help За дополнительной информацией"
    await message.reply_text(welcomed, reply_markup=joinButton)
    aumentare  StopPropagation
