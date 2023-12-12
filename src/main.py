import os
import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']
tg_bot_token = os.environ['TG_BOT_TOKEN']

messages = [{
  "role": "system",
  "content": "You are the ever faithful and helpful assistant named byte buddy. Limit any provided answer to 300 words or less regardless of what is asked."
}]

logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO)

async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
  messages.append({"role": "user", "content": update.message.text})
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
  
  completion_answer = completion['choices'][0]['message']['content']
  messages.append({"role": "assistant", "content": completion_answer})

  await context.bot.send_message(chat_id=update.effective_chat.id, text=completion_answer)
  return {"statusCode": 200, "body": completion_answer}

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="I'm a bot, please talk to me!")
  return {"statusCode": 200, "body": response_text}


if __name__ == '__main__':
  application = ApplicationBuilder().token(tg_bot_token).build()

  start_handler_func = CommandHandler('start', start_handler)
  chat_handler_func = MessageHandler(filters.TEXT & (~filters.COMMAND), chat_handler)

  application.add_handler(chat_handler_func)
  application.add_handler(start_handler_func)

  application.run_polling()
