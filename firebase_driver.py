import pyrebase

from config import config

firebase = pyrebase.initialize_app(config)

db = firebase.database()
storage = firebase.storage()


storage.child("images").put("example.jpg")