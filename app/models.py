from app import db
from datetime import datetime


class User(db.Model):
	__tablename__ = "User"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(130), unique=True, nullable=False)
	about_me = db.Column(db.String(100))
	pass_hash = db.Column(db.String(200), nullable=False)
	avatar = db.Column(db.String(255), nullable=False)
	phone = db.Column(db.String(11))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)


class Post(db.Model):
	__tablename__ = "Post"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(50))
	body = db.Column(db.String(200))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	post_date = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.title)
