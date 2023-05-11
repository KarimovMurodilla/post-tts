import aiohttp
from uuid import uuid4
from pathlib import Path


class Muxlisa:
    def __init__(self):
        self.__api = "https://api.muxlisa.uz/v1/tts/?text="
        self.__dir = Path(__file__).resolve().parent / 'audio_results'
    
    async def text_to_speech(self, text):
        url = self.__api + text
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                audio_file_bytes = await resp.content.read()

            file_name = uuid4()
            dist = self.__dir / f'{file_name}.mp3'
            with open(dist, 'wb') as f:
                f.write(audio_file_bytes)
        
        return dist