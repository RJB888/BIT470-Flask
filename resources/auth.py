from flask_restful import Resource, reqparse
import jwt
import src.const
from src.db import get_db

parser = reqparse.RequestParser()

class Signup(Resource):
    def post(self):
        """This method adds new user to the db. And returns that user's un and a jwt."""
        parser.add_argument('username')
        parser.add_argument('password')
        data = parser.parse_args()
        un = data['username']
        pw = data['password']
        pw_hash = hash(pw)
        userid = hash(un)
        token = jwt.encode({"password": pw}, src.const.SECRET_KEY, algorithm="HS256")
        try: # TODO: check db for duplicate un?
            get_db().cursor().execute(f'INSERT INTO users(id, username, password) VALUES({userid}, "{un}", "{pw_hash}")')
            get_db().commit()
            get_db().close()
            success = True
        except Exception as err:
            print(err)
            success = False

        good_response = {
            "success": success,
            "payload": {
                "userid": userid,
                "username": un,
                "token": token
            }
        }
        fail_response = {
            "success": success,
            "text": "Failed to add user. Check you information and try again."
        }
        return good_response if success else fail_response

class Login(Resource): #TODO: write the login route
    def post(self):
        """This method will log the user in"""
        return {"message": "Coming soon"}
    
