import os
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# токен берётся из Render (Environment Variables)
TOKEN = os.getenv("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return

    text = update.message.text.lower()

    # ищем все "мя"
    matches = re.findall(r'мя', text)
    count = len(matches)

    if count > 0:
        if count > 30:
            count = 30

        await update.message.reply_text("мя" * count)


app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
