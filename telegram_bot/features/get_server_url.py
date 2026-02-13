import requests
import logging
import socket
from urllib.parse import urlparse
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

help_str = "/server - View SSH server address and port"

async def get_server_addr(update: Update, context: ContextTypes.DEFAULT_TYPE):
  try:
    hostname = socket.gethostname()
  except Exception as ex:
    logging.error(f"Error retrieving SSH server address: {ex}")
    return await update.message.reply_text("Error retrieving SSH server address.")

  await update.message.reply_text(
    f"SSH server address: `{hostname}:2222`\n"
    "Remember to connect to your Tailnet before SSHing in or running rsync\!",
    parse_mode=ParseMode.MARKDOWN_V2,
  )

def add_handlers(application: Application):
  application.add_handler(CommandHandler("server", get_server_addr))
