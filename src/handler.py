from telegram import Update
from telegram.ext import CallbackContext
from models import process_message

async def start_command(update: Update, context: CallbackContext) -> None:
    start_message = "Welcome to the Employee Chatbot! Type /help to see available commands."
    await update.message.reply_text(start_message)
    print(f'Command: start')
    print('Bot: ', start_message )

async def help_command(update: Update, context: CallbackContext) -> None:
    help_message = "You can ask about HR policies, leave management, and more!"
    await update.message.reply_text(help_message)
    print(f'Command: help')
    print('Bot: ', help_message)

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = process_message(user_input)
    await update.message.reply_text(response)
    # Print to output
    message_type = update.message.chat.type
    print(f'user ({update.message.chat.id}) in ({message_type}): "{user_input}"'.encode('ascii', 'ignore').decode())
    print('Bot:', response)


async def error(update: Update, context:CallbackContext):
    print(f'Update {update} caused error {context.error}')
