from aiogram import types

from loader import dp, tts


@dp.channel_post_handler()
async def process_tts(message: types.Message):  
    result_dir = await tts.text_to_speech(message.text)
    await message.reply_audio(types.InputFile(result_dir))
    
