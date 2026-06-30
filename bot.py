from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import BOT_TOKEN
from database import create_tables

from handlers.start import start
from handlers.coin import coin_handler
from telegram.ext import CallbackQueryHandler
from handlers.timeframe import timeframe_handler



def main():

    create_tables()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
     CallbackQueryHandler(timeframe_handler)
    )

    app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, coin_handler)
    )
    

    print("🚀 Coin AI Bot ishga tushdi...")

    app.run_polling()


if __name__ == "__main__":
    main()