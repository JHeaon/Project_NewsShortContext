import telegram
import os


class TelegramController():

    @classmethod
    async def send_telegram_message(cls, message: str):
        """
        chat_id 는 https://api.telegram.org/bot[telegram http_api_token]]/getUpdates 으로 확인 가능
        """
        bot: str = telegram.Bot(token=os.getenv("HTTP_API"))
        chat_id: int = os.getenv("CHAT_ID")
        
        await bot.send_message(chat_id, message)