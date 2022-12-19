import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

openai.api_key = ""

telegram_bot_token = ""

def generate_response(input_text):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=input_text,
    max_tokens=2048,
    n=1,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

def handle_message(update, context):
  input_text = update.message.text
  response = generate_response(input_text)
  context.bot.send_message(chat_id=update.message.chat_id, text=response)

def error_callback(update, context):
  try:
    raise context.error
  except Exception as e:
    print(e)

updater = Updater(telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

# Add the error handler
dispatcher.add_error_handler(error_callback)

updater.start_polling()