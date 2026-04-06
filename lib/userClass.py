from .databaseClass import Mdbconn as MConn
from bcrypt import hashpw, gensalt, checkpw
from pymongo.errors import DuplicateKeyError
from flask import session 
from .errorClass import DuplicateUserError, NotFoundUserError, PasswordError
from .SessionClass import Session
class User:

    @staticmethod
    def login(user_info,request):
        #TODO:inset validation 
        
        db_conn = MConn.getMongoClient()
        result = db_conn['users'].find_one({'username' : user_info['username']})
        if not result:
            raise NotFoundUserError()
        if not checkpw(user_info['password'].encode(),result['password']):
            raise PasswordError()
        
        return result['username']
        
    @staticmethod
    def signup(user_info):
        db_conn = MConn.getMongoClient()
        user_info['password'] = hashpw(user_info['password'].encode(),gensalt())
        try:
            db_conn.users.insert_one(user_info)
        except DuplicateKeyError:
            raise DuplicateUserError()
        except Exception as e:
            raise Exception('An unexpected error occured :'+ str(e))
