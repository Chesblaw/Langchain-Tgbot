from telegram.ext import  CommandHandler, MessageHandler, filters, Application
from handler import start_command, help_command, handle_message, error
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

def main():
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))    
    app.add_handler(CommandHandler('help', help_command))    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error) 

    print("polling...")
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()
