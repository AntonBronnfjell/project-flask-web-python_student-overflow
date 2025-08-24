from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

question_tags = db.Table(
    "question_tags",
    db.Column("question_id", db.Integer, db.ForeignKey("question.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    body_md = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.relationship("Tag", secondary=question_tags, backref="questions")

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body_md = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)