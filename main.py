import telegram
from telegram import ChatPermissions
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import random
import asyncio
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
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

app = ApplicationBuilder().token("6138874795:AAF2itswGW-mjSgcp6AeCJxboDRQkaz0ST8").build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("coinflip", coinflip))
#app.add_handler(CommandHandler("hack", hack))
app.add_handler(CommandHandler("help", help_handler))

app.run_polling()