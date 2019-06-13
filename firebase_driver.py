import pyrebase

from config import config

firebase = pyrebase.initialize_app(config)

db = firebase.database()
storage = firebase.storage()
temp_file_path = '.temp/file.jpg'


def get(source):
    storage.child("images").child(source).download(temp_file_path)
    return temp_file_path


def upload(file, source):
    storage.child('images').child(source).put(file)
