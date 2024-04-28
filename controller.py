from db import db, Visitor
from uuid import uuid4
import os

def handle_new_visitor():
    visitor_id = str(uuid4())
    visitor = Visitor(identifier=visitor_id)
    db.session.add(visitor)
    db.session.commit()
    return f"Welcome, new visitor! You are uniquely identified by {visitor_id}", visitor_id

def get_visitor_welcome_back_message(visitor_id):
    return f"Welcome back, visitor {visitor_id}!"

def get_app_version():
    version = os.getenv('APP_VERSION', '1.0.0')  # Provide a default in case it's not set
    return {"version": version}