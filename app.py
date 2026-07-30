import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("📊 تحلیل بازارها", callback_data="markets"),
            InlineKeyboardButton("🤖 مشاور سرمایه‌گذاری", callback_data="advisor")
        ],
        [
            InlineKeyboardButton("💼 پرتفوی من", callback_data="portfolio"),
            InlineKeyboardButton("🚨 هشدارهای بازار", callback_data="alerts")
        ],
        [
            InlineKeyboardButton("📰 اخبار مالی", callback_data="news"),
            InlineKeyboardButton("📚 آموزش سرمایه‌گذاری", callback_data="education")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام 👋\n\n"
        "من MoneyMentor AI هستم.\n"
        "دستیار هوشمند سرمایه‌گذاری شما.\n\n"
        "لطفاً یک گزینه را انتخاب کنید:",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    answers = {
        "markets": "📊 تحلیل بازارها به زودی فعال می‌شود.",
        "advisor": "🤖 مشاور سرمایه‌گذاری هوشمند در حال آماده‌سازی است.",
        "portfolio": "💼 بخش ساخت و مدیریت پرتفوی در حال توسعه است.",
        "alerts": "🚨 سیستم هشدار هوشمند بازار اضافه خواهد شد.",
        "news": "📰 تحلیل اخبار اقتصادی به زودی فعال می‌شود.",
        "education": "📚 آموزش‌های مالی آماده می‌شود."
    }

    await query.edit_message_text(
        answers.get(query.data, "گزینه نامعتبر")
    )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("MoneyMentor AI Bot Started ✅")

    app.run_polling()


if __name__ == "__main__":
    main()
