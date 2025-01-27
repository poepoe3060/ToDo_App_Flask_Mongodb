from application import app
from flask_pymongo import PyMongo


app.config["SECRET_KEY"] = "56dbb76de41e1376094d3b05fd35cde93909f4ea"
app.config['MONGO_URI'] = "mongodb+srv://root:root@cluster0.u3ckb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MongoDB setup
mongodb_client = PyMongo(app)
database = mongodb_client.db


if __name__ == "__main__":
    app.run(debug=True)
