from datetime import date
from flask_restful import Resource, reqparse
from flask import jsonify
from src.db import get_db

import src.const

parser = reqparse.RequestParser()

class User(Resource):
    def get(self, user_name):
        """This method returns a given user's information"""
        result = get_db().cursor().execute(f'SELECT * FROM users WHERE username="{user_name}"')
        row = result.fetchone()
        return dict(zip([c[0] for c in result.description], row))
    def post(self): #TODO: maybe delete this? Moved to the signup method in auth
        return
class Users(Resource):
    """This method returns an array of all the users."""
    def get(self):
        result = get_db().cursor().execute('SELECT * FROM users')
        rows = result.fetchall()
        get_db().close()
        response = []
        for row in rows:
            response.append(dict(zip([c[0] for c in result.description], row)))
        return response
