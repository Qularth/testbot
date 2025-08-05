from telebot.async_telebot import AsyncTeleBot
import asyncio
import os
from src import handlers #NoQa 


bot = AsyncTeleBot(os.environ["ECHOFROST_TG_TOKEN"])



if __name__=='__main__':
    asyncio.run(bot.polling())