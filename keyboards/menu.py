from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils.constants import *

def main_menu_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "📊 Oddiy analiz",
                callback_data=CB_FREE_ANALYSIS
            )
        ],

        [
            InlineKeyboardButton(
                "🤖 AI Analiz ⭐ PRO",
                callback_data=CB_AI_ANALYSIS
            )
        ],

        [
            InlineKeyboardButton(
                "🔄 Coinni almashtirish",
                callback_data=CB_CHANGE_COIN
            )
        ],

        [
            InlineKeyboardButton(
                "⏰ Timeframe almashtirish",
                callback_data=CB_CHANGE_TIMEFRAME
            )
        ],

        [
            InlineKeyboardButton(
                "📈 Grafik",
                callback_data=CB_CHART
            ),

            InlineKeyboardButton(
                "👤 Profil",
                callback_data=CB_PROFILE
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)