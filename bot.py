from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой ИИ-бот 🤖")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Бот запущен")
app.run_polling()
