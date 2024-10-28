from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import final

# Define constants for bot token and username
TOKEN_: final = '7800350707:AAE4Aa1qJ_NsUnyFLkXy-xaw4ZNzL9qjswY'
BOT_USERNAME_: final = '@BermudezLVbot'

# Define command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a Python bot. Please type something so I can respond!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

# Function to process text and return a response
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hola' in processed:
        return "Hey!"

    if 'como estas' in processed:
        return "I am good!"

    if 'me gusta python' in processed:
        return "Nice, me too!"

    return "No entiendo nada."

# Define handle message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME_ in text:
            new_text: str = text.replace(BOT_USERNAME_, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # If the bot is not mentioned in a group chat, ignore the message
    else:
        response: str = handle_response(text)

    print('bot:', response)
    await update.message.reply_text(response)

# Define error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update... {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(TOKEN_).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Register error handler
    app.add_error_handler(error)

    # Start polling
    print("Polling...")
    
    app.run_polling(poll_interval=3)
