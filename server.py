from flask import Flask, render_template, redirect, session,request
from werkzeug.utils import secure_filename
from src import get_config 
from src.User import User
import requests
from src.telegram_class import telegram
import os
import threading
import json


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for Flask sessions
app.config['UPLOAD_FOLDER'] = "/home/kali/telegram_server/files"
token = get_config("bot_token")
app.config['chat_id'] = get_config("chat_id")
app.config['url_get_updates'] = f"https://api.telegram.org/bot{token}/getUpdates"
app.config['url_send_documentd'] = f'https://api.telegram.org/bot{token}/sendDocument'


instaloader_running = False
@app.route('/')
def show():
   conten=User.show()
   print(conten)
   return render_template('show.html',content=conten)


@app.route('/upload')
def upload():
    # session['session_py'] = session_py
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file= request.files['file']
      filename = secure_filename(file.filename)
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      file.save(file_path)
      chat_id= app.config['chat_id']
      url_send_document= app.config['url_send_documentd']
      data =telegram.send_files(chat_id,file_path,url_send_document)
      User.insert1(data)
      os.popen("rm -rf /home/kali/telegram_server/files/*").read()

      return redirect("/upload")
   
# @app.route('/show')
# def show():
#    conten=User.show()
#    print(conten)
#    return render_template('show.html',content=conten)

@app.route('/rec1')
def rec1():
    # session['session_py'] = session_py
    return render_template('rec.html')

@app.route('/rec', methods = ['GET', 'POST'])
def rec():
   if request.method == 'POST':
      text_field_value = request.form.get('text_field')
      file_id=User.rec(text_field_value)      
      chat_id= app.config['chat_id']
      url_send_document= app.config['url_send_documentd']
      data1=telegram.recvice_files(chat_id,file_id,url_send_document)
      User.insert2(data1)
      return redirect("/upload")



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=4000, debug=True)
