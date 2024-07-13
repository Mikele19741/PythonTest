from telegram import   InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import  ApplicationBuilder, ConversationHandler,CommandHandler, ContextTypes, CallbackQueryHandler
import bot
TELEGRAM_BOT_TOKEN=''
TELEGRAM_URL='t.me/test_solutions_bot'
def main():
   
    app=ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CallbackQueryHandler(bot.gender_callback,ContextTypes.DEFAULT_TYPE))

    app.run_polling()


if __name__ == '__main__':
    main()
