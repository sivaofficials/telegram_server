import requests

class telegram:
    def __init__(self,data):
          print("{} the id".format(data))
          

    @staticmethod
    def send_files(chat_id,path_file,url_send_document):
            data = {'chat_id': chat_id}
            files = {'document': open( path_file, 'rb')}
            response_send_document = requests.post(url_send_document, files=files, data=data)
            data = response_send_document.json()
            data1={
                "chat_id":chat_id,
                "date":data['result']['date'],
                "username":data['result']["chat"]["username"],
                "date":data['result']['date'],
                "file_name":data['result']["document"]['file_name'],
                "file_id":data['result']["document"]['file_id'],
                "file_size":data['result']["document"]['file_size']
                }
            return data1
    
    @staticmethod
    def recvice_files(chat_id,document_file_id,url_send_document):          
        files = {'document': (None, document_file_id)}
        data = {'chat_id': chat_id}
        response = requests.post(url_send_document, files=files, data=data)
        data = response.json()
        data1={
                "chat_id":chat_id,
                "date":data['result']['date'],
                "username":data['result']["chat"]["username"],
                "date":data['result']['date'],
                "file_name":data['result']["document"]['file_name'],
                "file_id":data['result']["document"]['file_id'],
                "file_size":data['result']["document"]['file_size']
                }
        return data1
