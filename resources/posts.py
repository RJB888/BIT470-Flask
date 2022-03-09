from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from distutils.log import info
from flask_restful import Api, Resource, reqparse
from flask import jsonify, request, Flask, render_template, request
from resources.models import app,db
from resources.models import User, Tweets


parser = reqparse.RequestParser()

class PostTweet(Resource):
    def post(self):
        parser.add_argument('tweet_text')
        data = parser.parse_args()
        postedtweet = data['tweet_text']
        tweets = Tweets(tweet_text=postedtweet)
        try:
            db.session.add(tweets)
            db.session.commit()
            success = True
        except Exception as err:
            print(err)
            success = True

        good_response = {
            "success": success,
            "payload": {
                "tweet": postedtweet            
            }
        }
        fail_response = {
            "success": success,
            "text": "Failed to add post. Check you information and try again."
        }
        return good_response if success else fail_response
