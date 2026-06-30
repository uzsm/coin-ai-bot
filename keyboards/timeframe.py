from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def timeframe_keyboard():

    keyboard = [

        [
            InlineKeyboardButton("5m", callback_data="TF_5M"),
            InlineKeyboardButton("15m", callback_data="TF_15M")
        ],

        [
            InlineKeyboardButton("1H", callback_data="TF_1H"),
            InlineKeyboardButton("4H", callback_data="TF_4H")
        ],

        [
            InlineKeyboardButton("1D", callback_data="TF_1D")
        ],

        [
            InlineKeyboardButton(
                "🔄 Coinni almashtirish",
                callback_data="CHANGE_COIN"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)