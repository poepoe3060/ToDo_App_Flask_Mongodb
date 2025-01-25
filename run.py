from application import app
from flask_pymongo import PyMongo


if __name__ == "__main__":
    app.run(debug=True)
    app.config("SECRET KEY") == "56dbb76de41e1376094d3b05fd35cde93909f4ea"
    app.config('MONGO_URI') == "mongodb+srv://root:root@cluster0.u3ckb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    #mongodb_setup
    mongodb_client = PyMongo(app)
    database = mongodb_client.database

    # mongodb+srv://root:root@cluster0.u3ckb.mongodb.net/