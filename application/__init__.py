import certifi
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "56dbb76de41e1376094d3b05fd35cde93909f4ea"
app.config["MONGO_URI"] = "mongodb+srv://poepoe:poepoe@cluster0.u3ckb.mongodb.net/todo_flask?retryWrites=true&w=majority"

# Pass certifi's CA file
mongodb_client = PyMongo(app, tlsCAFile=certifi.where())
db = mongodb_client.db  

from application import routes
