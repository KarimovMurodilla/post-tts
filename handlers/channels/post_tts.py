import re
from aiogram import types

from utils.misc.tts.muxlisa import Muxlisa
from loader import dp, db


@dp.channel_post_handler()
async def process_tts(message: types.Message):
    tts = Muxlisa()

    pattern = re.compile(r"https?://\S+")
    text_without_links = pattern.sub("", message.text)

    result_dir = await tts.text_to_speech(text_without_links, message)
    await message.reply_audio(types.InputFile(result_dir))

    chat_id_db = await db.get_channel(message.chat.id)
    if not chat_id_db:
        await db.reg_channel(message.chat.id, message.chat.title)
    
    await db.reg_audio(message.chat.id, message.text, str(result_dir))