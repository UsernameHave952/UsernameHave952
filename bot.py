from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot tokeni
TOKEN = '8179675229:AAHl909G5kvZ5-BX0yeixQMEtecGqQegqG8'

# /start buyruqni qayta ishlash uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # "Copilotni ochish" tugmachasi bilan klaviatura yaratish
    keyboard = [[InlineKeyboardButton("Copilotni ochish", url="https://t.me/Microsoftcom_bot/azzcop")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Xabarni yuborish
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Salom! Men bilan Copilotdan foydalanishingiz mumkin.", reply_markup=reply_markup)

# Botni ishga tushirish
app = ApplicationBuilder().token(TOKEN).build()

# Buyruqlarni ro'yxatga olish
app.add_handler(CommandHandler('start', start))

# Botni ishga tushirish
app.run_polling()
