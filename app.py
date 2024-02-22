from src import get_config 
from src.User import User
import requests
from src.telegram_class import telegram
import time

token = get_config("bot_token")
chat_id = get_config("chat_id")

# Corrected URL for getting updates
url_get_updates = f"https://api.telegram.org/bot{token}/getUpdates"
# Corrected URL for sending a document
url_send_document = f'https://api.telegram.org/bot{token}/sendDocument'

url_send_document = f'https://api.telegram.org/bot{token}/sendMessage'

path_file="/home/kali/python_instawebsite/server.py"
document_file_id="BQACAgUAAxkDAAIEjmXWFL2wJmL0EWugXhAEsn0USpbLAAICDQACp9ywVqmpVEjpDkE1NAQ"
 
data =telegram.send_files(chat_id,path_file,url_send_document)
print(data)
data1=telegram.recvice_files(chat_id,document_file_id,url_send_document)
print(data1)
bg1 =User.insert1(data)
print(bg1)
bg =User.insert2(data1)
print(bg)