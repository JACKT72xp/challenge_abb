from flask import Flask
from db import db, init_db
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')

    db.init_app(app)
    init_db(app)
    return app

app = create_app()
from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)  # Set host to '0.0.0.0' and debug to True


