
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

ADMIN_ID = os.getenv("ADMIN_ID")
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_message = (
        f"👋 Welcome to Omnira AI Global, {user.first_name}!

"
        "✨ I’m your intelligent assistant — here to guide you in crypto, stocks, life decisions, and much more.

"
        "💡 Available Plans:
"
        "• Omnira Basic (Free)
"
        "• Omnira Pro – $50 (USDT/BTC)
"
        "• Omnira Crypto+ – $100 (USDT/BTC)

"
        "Type anything to get started, or use the menu below."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
