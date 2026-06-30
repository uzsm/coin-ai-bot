from telegram import Update
from telegram.ext import ContextTypes

from database import get_user
from services.analysis_service import analyze


async def analyze_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = get_user(update.effective_user.id)

    if not user:
        return

    result = analyze(
        user["selected_coin"],
        user["timeframe"]
    )

    text = f"""
🪙 Coin: {result['symbol']}

⏰ Timeframe: {result['timeframe']}

📈 Trend: {result['trend']}

📊 Pivot: {result['stats']['pivot_count']}

📉 Swing: {result['stats']['swing_count']}

🏗 Structure: {result['stats']['structure_count']}

💥 BOS: {result['stats']['bos_count']}
"""

    await update.message.reply_text(text)