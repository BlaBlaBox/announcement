from flask_sqlalchemy import SQLAlchemy
from announcement_config import app

db = SQLAlchemy(app)

class announce(db.Model):
	announcement_id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(30),nullable=False)
	text = db.Column(db.String(300),nullable=False)
	image_link = db.Column(db.String(300),nullable=False)
	movie_link = db.Column(db.String(300),nullable=False)


def add_announcement(title,text,image_link,movie_link):
	new_announcement = announce(title=title,text=text,image_link=image_link,movie_link=movie_link)
	db.session.add(new_announcement)
	db.session.commit()
	return new_announcement

def get_announcements():
    announcements = announce.query.all()
    return None if announcements == [] else announcements

db.create_all()