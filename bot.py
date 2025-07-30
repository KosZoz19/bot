import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from dotenv import load_dotenv
load_dotenv()

# Poprawne pobieranie zmiennych środowiskowych
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
bot_token = os.getenv("TELEGRAM_TOKEN")
onlyfans_link = os.getenv("ONLYFANS_LINK")

user_messages = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in user_messages:
        user_messages[user_id] = []

    user_messages[user_id].append(text)

    if len(user_messages[user_id]) == 5:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"👙 Jeśli chcesz więcej… zobacz: {onlyfans_link}")
        return

    prompt = f"Jesteś atrakcyjną dziewczyną flirtującą z użytkownikiem. Odpowiadaj seksownie i zmysłowo. On napisał: {text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    reply = response.choices[0].message.content
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hej! Napisz coś do mnie 💬")

def main():
    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot działa!")
    app.run_polling()

if __name__ == '__main__':
    main()
