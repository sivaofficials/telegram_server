import requests
import json


bot_token = "6932200060:AAHF5T64BrgwlTuGnxROifxadYFzv5k2spM"
chat_id = "2076098803"

# Corrected URL for getting updates
url_get_updates = f"https://api.telegram.org/bot{bot_token}/getUpdates"

# Corrected URL for sending a document
url_send_document = f'https://api.telegram.org/bot{bot_token}/sendDocument'


files = "/home/kali/python_instawebsite/server.py"
file_id = 'BQACAgUAAxkDAAIEd2XUyyAvMBsi7Hx8o497in8ir1b8AAIuDgAC3ZuoVo1c1oZWFxLENAQ'



def send_document_save(chat_id, path_file):
    data = {'chat_id': chat_id}
    files = {'document': open( path_file, 'rb')}
    response_send_document = requests.post(url_send_document, files=files, data=data)
    data = response_send_document.json()
    print(data['result'])


send_document_save(chat_id,files)

def send_document_server(chat_id, document_file_id):
    files = {'document': (None, document_file_id)}
    data = {'chat_id': chat_id}
    response = requests.post(url_send_document, files=files, data=data)
    data = response.json()
    print(data)

# send_document_server(chat_id,file_id)