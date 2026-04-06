
from mongogettersetter import MongoGetterSetter
from lib.databaseClass import Mdbconn as MConn
# Connect to the MongoDB database and collection

db = MConn.getMongoClient()
collection = db.sessions
# Wrapper for MongoDB Collection with metaclass, use this inside your actual class.
class EmployeeCollection(metaclass=MongoGetterSetter):
    def __init__(self, _id):
        self._filter_query = {"id": _id} # or the ObjectID, at your convinence
        self._collection = collection # Should be a pymongo.MongoClient[database].collection

class Employee:
    def __init__(self, _id):
        self._filter_query = {"id": _id}
        self._collection = collection
        self.collection = EmployeeCollection(_id)

        # Create a new document if it doesn't exist
        if self.collection.get() is None:
            self._collection.insert_one(self._filter_query)
    
    def someOtherOperation(self):
        self.collection.hello = "Hello World"