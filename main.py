import asyncio
from src import handlers
from src.common import bot #NoQa 

if __name__=='__main__':
    asyncio.run(bot.polling())