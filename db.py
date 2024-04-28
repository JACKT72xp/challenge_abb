from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(50), unique=True, nullable=False)
    visit_date = db.Column(db.DateTime, default=db.func.current_timestamp())

def init_db(app):
    with app.app_context():
        db.create_all()
