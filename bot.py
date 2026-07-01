from telegram.ext import Application, CommandHandler
from config import TOKEN
from handlers import start

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущен!")

app.run_polling()
