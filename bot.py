import os
import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram.update import Update

openai.api_key = os.getenv("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")
bot_token = os.getenv("8376853322:AAGCUgsNiGhipaedYvNPHCI4MSH3nS_WcnE")
onlyfans_link = os.getenv("ONLYFANS_LINK")

user_messages = {}

def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in user_messages:
        user_messages[user_id] = []

    user_messages[user_id].append(text)

    if len(user_messages[user_id]) == 5:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"👙 Jeśli chcesz więcej… zobacz: {onlyfans_link}")
        return

    prompt = f"Jesteś atrakcyjną dziewczyną flirtującą z użytkownikiem. Odpowiadaj seksownie i zmysłowo. On napisał: {text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    reply = response.choices[0].message.content
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
