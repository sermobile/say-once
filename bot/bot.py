import os
import logging
from datetime import datetime
from pathlib import Path
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

INBOX_DIR = Path(os.environ["INBOX_DIR"])
ALLOWED_USER_ID = int(os.environ["ALLOWED_USER_ID"])

INBOX_DIR.mkdir(parents=True, exist_ok=True)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ALLOWED_USER_ID:
        await update.message.reply_text("Нет доступа.")
        return

    text = update.message.text or update.message.caption or ""
    if not text:
        await update.message.reply_text("Пришли текст примера.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = INBOX_DIR / f"{timestamp}.md"
    filename.write_text(text, encoding="utf-8")

    await update.message.reply_text(f"Сохранено: {filename.name}")


def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT | filters.CAPTION, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()
