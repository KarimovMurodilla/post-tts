import re
from aiogram import types

from loader import dp, tts, db


@dp.channel_post_handler()
async def process_tts(message: types.Message):
    pattern = re.compile(r"https?://\S+")
    text_without_links = pattern.sub("", message.text)

    result_dir = await tts.text_to_speech(text_without_links)
    await message.reply_audio(types.InputFile(result_dir))

    chat_id_db = await db.get_channel(message.chat.id)
    if not chat_id_db:
        await db.reg_channel(message.chat.id, message.chat.title)
    
    await db.reg_audio(message.text, str(result_dir))