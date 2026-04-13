from mongogettersetter import MongoGetterSetter
from .databaseClass import Mdbconn as MConn
from flask import session
from uuid import uuid4
from time import time
import hashlib

db = MConn.getMongoClient()

class APIKeyCollection(metaclass=MongoGetterSetter):
    def __init__(self, id):
        self._collection = db.apikeys
        self._filter_query = {'$or' : [
            {"id": id},
            {"hash": id}
        ]}

class APIKey:

    def __init__(self, id):
        try:
            self.collection = APIKeyCollection(id)
            self.id = self.collection.id
        except Exception as e:
            return None
    
    def is_valid(self):
        creation_time = self.collection.creation_time
        validity = self.collection.validity
        if validity == 0:
            return True
        else:
            now = time()
            return now - creation_time < validity
    @staticmethod
    def get_api_key_info():
        if not session.get('authenticated') or not session.get('username'):
            raise Exception("Authentication required")
        
        collection = db.apikeys
        api_keys= collection.find({"username": session['username']})
        return api_keys
        
            
    @staticmethod
    def create_api_key(session , name, group,remark, request= None, validity=0,_type='api'):
        if not session.get('authenticated'):
            raise Exception("Authentication required")
        uuid = str(uuid4())
        collection = db.apikeys
        

        if request is not None:
            request_info = {
                'ip': request.remote_addr,
                'user_agent': request.headers.get('User-Agent'),
                'method': request.method,
                'url': request.url,
                'headers': dict(request.headers),
                'data': request.get_data().decode('utf-8')
            }
        else:
            request_info = None
        
        collection.insert_one({
            "id": uuid,
            "hash" : hashlib.md5(uuid.encode()).hexdigest(),
            "username": session['username'],
            "name": name,
            "group": group, 
            "remark": remark,
            "creation_time": time(),
            "validity": validity, # 0 means never expire
            "active": True,
            "type": _type,
            "request": request_info
        })  

        return APIKey(uuid)