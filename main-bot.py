from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = 'TELEGRAM_API_ID'
api_hash = 'TELEGRAM_API_HASH'

with TelegramClient('anon', api_id, api_hash) as client:
    for message in client.iter_messages('kwork_kwork', limit=10):
        print(message.text)
