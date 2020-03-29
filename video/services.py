import asyncio
import time

from video.handlers.video_info import VideoData

"""
class RunForever:
    async def work():
        while True:
            await asyncio.sleep(2)
            print('Task Executed')
            # VideoData().insert_data()

    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(work())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print('Closing Loop')
        loop.close()
"""


def video_scheduler():
    flag = True
    while flag:
        interval = 10
        result = VideoData().insert_data()
        flag = result
        print(f'Running In every - {interval}')
        time.sleep(interval)
