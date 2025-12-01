from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
import os
from dotenv import load_dotenv
# Загружает переменные из .env файла в переменные окружения
load_dotenv()

from gpt import *
from util import *


# тут будемо писати наш код :)
async def start(update, context):
    msg = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, msg)
    await show_main_menu(update, context, {
        "start": "Головне меню",
        "profile": "Генерація Tinder-профіля \uD83D\uDE0E",
        "opener": "Повідомлення для знайомства \uD83E\uDD70",
        "message": "Переписка від вашого імені \uD83D\uDE08",
        "date": "Спілкування з зірками \uD83D\uDD25",
        "gpt": "Задати питання ChatGPT \uD83E\uDDE0"
    })

async def hello(update, context):
    #await send_text(update, context, "Hello " + update.message.text)
    await send_text_buttons(update, context, "Hello " + update.message.text, {
        "start": "START",
        "stop": "STOP"
    })
async def buttons_handler(update, context):
    query = update.callback_query.data
    if query == "start":
        await send_text(update, context, "Started!")
    elif query == "stop":
        await send_text(update, context, "Stopped!")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
app.add_handler(CallbackQueryHandler(buttons_handler))
app.run_polling()
