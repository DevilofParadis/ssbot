import logging
from bot.screenshotbot import ScreenShotBot
from bot.config import Config

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
    logging.getLogger("pyrogram").setLevel(
        logging.INFO if Config.DEBUG else logging.WARNING
    )

    bot = ScreenShotBot()
    bot.run()
    
