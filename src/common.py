from telebot.async_telebot import AsyncTeleBot

import os

bot = AsyncTeleBot(os.environ["ECHOFROST_TG_TOKEN"])


