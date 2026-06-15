import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8975717406:AAGssAo6nkZo65LZQosPxa6K2Ybi6iXd7wg"

# защита от зацикливания
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return

    text = update.message.text.lower()

    # считаем все "мя" в тексте
    matches = re.findall(r'мя', text)
    count = len(matches)

    if count > 0:
        # защита от слишком длинного спама
        if count > 30:
            count = 30

        await update.message.reply_text("мя" * count)


app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
