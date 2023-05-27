import schedule
import time

from typing import List, Tuple
from dotenv import load_dotenv

from youtube_process import YoutubeController
from chatgpt_process import ChatgptController
from telegram_process import TelegramController
from selenium_process import SeleniumController

import asyncio

load_dotenv()

def run():
    
    """
    FIXME: chat gpt로 한번에 보내서 받을 수 있는 답변은 7개라서, 7개만 받는 형식으로 진행하여야 할듯
    """
    youtube_url_list: List[Tuple[str, str]] = SeleniumController.crawling()
    print(len(youtube_url_list), youtube_url_list)
    youtube_controller: YoutubeController = YoutubeController()
    
    
    try:
        for title, url in youtube_url_list:
            youtube_controller.set_youtube_url(url)
            youtube_korean_scripts: str = youtube_controller.get_korean_script()
            chat_gpt_context: str = ChatgptController.reduce_content(youtube_korean_scripts)
            asyncio.run(TelegramController.send_telegram_message(chat_gpt_context + "\n\n" + "[Youtube] " + url))
    except:
        pass
    

time_list = [str(i).zfill(2) + ":00" for i in range(25)]

for time in time_list:
    schedule.every().day.at(time).do(run)

while True:
    schedule.run_pending()