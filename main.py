from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN:final = "7528652491:AAGmT2vnGJZDyYAJX-vXPFLG-QDu8V8C6VQ"
BOT_USERNAME:final = "@text_ASCII_art_bot"



# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.replay_text("Hello, World!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.replay_text("HELP command!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.replay_text("cunstom command!")
 


# Responses
def handle_response(text: str) -> str:

    processed:str = text.lower()#Todo: try removing str

    if "hello" in text:
        return "Hi, there!"
    
    if "how are you" in text:
        return "It's okay. I'm a bot and I don't have feelings so my \"okay\" is just a text put by a programer"
    
    if "i love web dev" in text:
        return "are you sick or something?"
    


async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type 
    text: str = update.message.text
    user_id: str = update.message.chat.id

    print("User %s in %s: \"%s\"",(user_id,message_type,text))
    

