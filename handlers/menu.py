from telegram import Update
from telegram.ext import ContextTypes

from database import (
    get_user,
    set_state,
)

from keyboards.timeframe import timeframe_keyboard
from keyboards.menu import main_menu_keyboard

from services.analysis_service import analyze

from utils.constants import *
from services.chart_service import create_chart


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user = get_user(query.from_user.id)

    if user is None:
        return

    data = query.data

    # ===========================
    # ODDIY ANALIZ
    # ===========================

    if data == CB_FREE_ANALYSIS:

        result = analyze(
            user["selected_coin"],
            user["selected_timeframe"]
        )

        price = f'{result["last_price"]:,.2f}'

        text = f"""
📊 Coin AI Analysis

🪙 Coin: {result["symbol"]}
💰 Price: {price} USDT
⏰ Timeframe: {result["timeframe"]}

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
"""

        await query.edit_message_text(
            text,
            reply_markup=main_menu_keyboard()
        )

        return

    # ===========================
    # COIN ALMASHTIRISH
    # ===========================

    elif data == CB_CHANGE_COIN:

        set_state(
            query.from_user.id,
            STATE_WAIT_COIN
        )

        await query.edit_message_text(
            "🪙 Yangi coin kiriting.\n\nMasalan:\nBTC\nETH\nSOL"
        )

        return

    # ===========================
    # TIMEFRAME ALMASHTIRISH
    # ===========================

    elif data == CB_CHANGE_TIMEFRAME:

        set_state(
            query.from_user.id,
            STATE_WAIT_TIMEFRAME
        )

        await query.edit_message_text(
            "⏰ Timeframe tanlang.",
            reply_markup=timeframe_keyboard()
        )

        return

    # ===========================
    # AI ANALIZ
    # ===========================

    elif data == CB_AI_ANALYSIS:

        await query.answer(
            "🤖 AI Analiz tez orada qo'shiladi.",
            show_alert=True
        )

        return

    # ===========================
    # CHART
    # ===========================

        # ===========================
    # CHART
    # ===========================

    elif data == CB_CHART:

        await query.answer("📈 Grafik tayyorlanmoqda...")

        filename = create_chart(
            user["selected_coin"],
            user["selected_timeframe"]
        )

        await context.bot.send_photo(
            chat_id=query.message.chat.id,
            photo=open(filename, "rb")
        )

        return

    # ===========================
    # PROFILE
    # ===========================

    elif data == CB_PROFILE:

        await query.answer(
            "👤 Profil moduli tayyorlanmoqda.",
            show_alert=True
        )

        return