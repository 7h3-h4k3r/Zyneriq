from .databaseClass import Mdbconn as MConn
from bcrypt import hashpw, gensalt, checkpw
from pymongo.errors import DuplicateKeyError
from flask import session 
from .errorClass import DuplicateUserError, NotFoundUserError, PasswordError
from .SessionClass import Session
from uuid import uuid4
from datetime import datetime
import random
from mongogettersetter import MongoGetterSetter

db_conn = MConn.getMongoClient()
db_user = db_conn.users

class UserCollection(metaclass=MongoGetterSetter):
    def __init__(self, username):
        self._collection = db_user
        self._filter_query = {"$or" : [{"id": username}, {"username": username}]}


class User:
    def __init__(self, id):
        self.collection = UserCollection(id)
        self.username = self.collection.username
        self.id = self.collection.id
        
    @staticmethod
    def login(user_info,request):
        #TODO:inset validation 
        try:
            result = db_user.find_one({'username': user_info['username']})
            if result:
                if checkpw(user_info['password'].encode(), result['password']):
                    sess = Session.register_session(result['username'], request=request)
                    return sess.id
                else:
                    raise PasswordError()
        except Exception as e:
            raise NotFoundUserError() from e
        
        
        
    @staticmethod
    def signup(user_info):
        uuid = str(uuid4())
        try:
            hashed_password = hashpw(user_info['password'].encode(), gensalt())
            db_user.insert_one({
                'id': uuid,
                'username': user_info['username'],
                'password': hashed_password,
                'email': user_info['email'],
                'created_at': datetime.utcnow(),
                'active': False,
                'active_token': random.randint(100000, 999999)
            })

            return uuid
        except DuplicateKeyError as e:
            raise DuplicateUserError() from e
        except Exception as e:
            raise ValueError("An error occurred during signup: " + str(e)) from e
