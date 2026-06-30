from telegram import Update
from telegram.ext import ContextTypes
from database import get_user, set_state, set_coin

from keyboards.timeframe import timeframe_keyboard
from database import get_user, set_state


async def coin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("========== coin_handler ishladi ==========")

    user = get_user(update.effective_user.id)

    print("USER =", user)

    if user is None:
        print("❌ User topilmadi!")
        return

    state = user["state"]

    print("STATE =", state)

    if state != "WAIT_COIN":
        print("❌ State WAIT_COIN emas.")
        return

    coin = update.message.text.upper().strip()

# Agar foydalanuvchi USDT yozmasa, avtomatik qo'shamiz
    if not coin.endswith("USDT"):
     coin += "USDT"

    print("COIN =", coin)
    
    if len(coin) > 10:
        print("❌ Coin uzunligi noto'g'ri.")
        await update.message.reply_text("❌ Coin nomi noto'g'ri.")
        return

    print("✅ Timeframe tugmalari yuborildi.")

    await update.message.reply_text(
        f"🪙 {coin} tanlandi.\n\n"
        "⏰ Timeframe tanlang.",
        reply_markup=timeframe_keyboard()
    )
    set_coin(update.effective_user.id, coin)

    set_state(update.effective_user.id, "WAIT_TIMEFRAME")

    print("STATE WAIT_TIMEFRAME ga o'zgartirildi.")