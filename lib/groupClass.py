from mongogettersetter import MongoGetterSetter
from .databaseClass import Mdbconn as MConn
from uuid import uuid4 
from flask import session
db = MConn.getMongoClient()

class GroupCollection(metaclass=MongoGetterSetter):
    def __init__(self, id):
        self._collection = db.groups
        self._filter_query = {
            '$or' : [
                {"id": id},
                {"name": id}
            ]
        }
    
class Group:

    def __init__(self, id):
        self.collection = GroupCollection(id)
        self.id = self.collection.id

    
    @staticmethod
    def register_group(group_name , group_desc):
        if session.get('authenticated') is None:
            raise Exception("Authentication required")
        
        uid = str(uuid4())
        collection = db.groups
        collection.insert_one({
            'id' : uid,
            'name':group_name,
            'description' : group_desc,
            'active': True
        })

        return Group(uid)

    @staticmethod
    def get_groups():
        collection = db.groups
        result = collection.find({})
        return list(result)