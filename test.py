import asyncio
from utils.misc.tts.muxlisa import Muxlisa


async def main():
    obj = Muxlisa()
    await obj.text_to_speech("Lorem ipsum diganakan")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())