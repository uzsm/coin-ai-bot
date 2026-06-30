from telegram import Update
from telegram.ext import ContextTypes

from database import add_or_update_user, set_state


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    
    add_or_update_user(update.effective_user)

    set_state(update.effective_user.id, "WAIT_COIN")
    
    
    await update.message.reply_text(
        "👋 Coin AI Bot ga xush kelibsiz!\n\n"
        "🪙 Coin nomini kiriting.\n\n"
        "Masalan:\n"
        "BTC\n"
        "ETH\n"
        "SOL"
    )