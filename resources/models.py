from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable = False)
    password = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    tweets = db.relationship('Tweets', backref ='author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    bio = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"Profile('{self.bio}')"


class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    tweet_text = db.Column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"Tweets('{self.userid}', '{self.tweet_text}', '{self.date_posted}')"


class User_Follows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    followed = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"User_Follows('{self.id}')"


class Tweet_Reactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable = False)
    reacting_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    reaction = db.Column(db.Boolean, nullable = False)

    def __repr__(self):
        return f"Tweet_Reactions('{self.tweet}', '{self.reacting_user}','{self.reaction}')"


class Tweet_Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    comment = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"Tweet_Comments('{self.tweet}', '{self.userid}', '{self.comment}' )"
