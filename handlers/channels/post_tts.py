from aiogram import types

from loader import dp, tts, db


@dp.channel_post_handler()
async def process_tts(message: types.Message):  
    result_dir = await tts.text_to_speech(message.text)
    await message.reply_audio(types.InputFile(result_dir))

    chat_id_db = await db.get_channel(message.chat.id)
    if not chat_id_db:
        await db.reg_channel(message.chat.id, message.chat.title)
    
    await db.reg_audio(message.text, str(result_dir))