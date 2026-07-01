from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋 Я твой будущий ИИ-бот 🤖"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        f"Ты написал:\n\n{text}"
    )
