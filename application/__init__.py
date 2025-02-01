from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "56dbb76de41e1376094d3b05fd35cde93909f4ea"
app.config["MONGO_URI"] = "mongodb+srv://poepoe:poepoe@cluster0.u3ckb.mongodb.net/todo_flask?retryWrites=true&w=majority"

mongodb_client = PyMongo(app)
db = mongodb_client.db  

try:
    print("Connected to MongoDB successfully!")
    print("Existing collections:", db.list_collection_names())  
except Exception as e:
    print("MongoDB Connection Error:", e)


from application import routes  
