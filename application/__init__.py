from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "56dbb76de41e1376094d3b05fd35cde93909f4ea"
app.config["MONGO_URI"] = "mongodb+srv://root:root@cluster0.u3ckb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes  
