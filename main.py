import traceback

import telegram
from telegram import *
from telegram.ext import *
import logging
import random
import json
import asyncio
from collections import namedtuple
def get(file):
    try:
        with open(file, encoding='utf8') as data:
            return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")


def traceback_maker(err, advance: bool = True):
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
config = get("config.json")
logger = logging.getLogger(__name__)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("test")
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hallo {update.effective_user.first_name}')
    logging.info("Ein Command wurde ausgeführt: hello")
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'test')
    logging.info("Ein Command wurde ausgeführt: hello")
async def coinflip(update: Update, context: ContextTypes.DEFAULT_TYPE,) -> None:
    coin = ["Kopf", "Zahl", "Die Münze ist Runtergefallen, bitte Versuche es Nochmal"]
    rancoin = random.choice(coin)
    await update.message.reply_text(f"**Münzwurf**\n\n Es ist {rancoin}")
async def hack(update: Update,context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Accessing Telegram Files... [▓▓    ]")
    await asyncio.sleep(2)
    await update.message.reply_text("Accessing Telegram Files... [▓▓▓   ]")
    await asyncio.sleep(2)
    await update.message.reply_text("Accessing Telegram Files... [▓▓▓▓▓ ]")
    await asyncio.sleep(2)

app = ApplicationBuilder().token(config.token).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("coinflip", coinflip))
#app.add_handler(CommandHandler("hack", hack))
app.add_handler(CommandHandler("help", help_handler))

app.run_polling()