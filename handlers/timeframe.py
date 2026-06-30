from telegram import Update
from telegram.ext import ContextTypes
from keyboards.menu import main_menu_keyboard

from database import (
    get_user,
    set_state,
    set_timeframe,
)
from services.analysis_service import analyze


from utils.constants import (
    STATE_MAIN_MENU,
    CB_TF_5M,
    CB_TF_15M,
    CB_TF_1H,
    CB_TF_4H,
    CB_TF_1D,

    TF_5M,
    TF_15M,
    TF_1H,
    TF_4H,
    TF_1D,
)


TIMEFRAME_MAP = {
    CB_TF_5M: TF_5M,
    CB_TF_15M: TF_15M,
    CB_TF_1H: TF_1H,
    CB_TF_4H: TF_4H,
    CB_TF_1D: TF_1D,
}


async def timeframe_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user = get_user(query.from_user.id)

    if user is None:
        return

    data = query.data

    print("CALLBACK =", data)

    if data not in TIMEFRAME_MAP:
        return

    timeframe = TIMEFRAME_MAP[data]
    print("=" * 40)
    print("USER =", dict(user))
    print("SELECTED COIN =", user["selected_coin"])
    print("=" * 40)
    set_timeframe(query.from_user.id, timeframe)

    result = analyze(user["selected_coin"], timeframe)

 

    set_state(query.from_user.id, STATE_MAIN_MENU)
    
    price = f'{result["last_price"]:,.2f}'

    await query.edit_message_text(
    f"""
📊 Coin AI Analysis

🪙 Coin: {user["selected_coin"]}
⏰ Timeframe: {timeframe}
💰 Price: {price} USDT

━━━━━━━━━━━━━━

📈 Trend:
{result["trend"]}

📍 Pivotlar:
{result["stats"]["pivot_count"]}

🌊 Swinglar:
{result["stats"]["swing_count"]}

🏗 Structure:
{result["stats"]["structure_count"]}

💥 BOS:
{result["stats"]["bos_count"]}

━━━━━━━━━━━━━━

Tanlang:
""",
    reply_markup=main_menu_keyboard()
)