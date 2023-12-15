from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    #CRUD operations for Animal collection in MongoDB
   

    def __init__(self, user, password, host, port, db, col):
        
        #Initialize the MongoClient and connect to the specified database and collection.
        
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[col]

    def create(self, data):
        
        #Insert a document into the specified MongoDB database and collection.
        #Return True if successful insert, else False.
        
        if data is not None:
            result = self.collection.insert(data)
            return True if result.inserted_id else False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query):
        
        #Query for documents from the specified MongoDB database and collection.
        #Return the result in a list if the command is successful, else an empty list.
        
        cursor = self.collection.find(query)
        result = [document for document in cursor]
        return result
