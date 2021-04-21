from pymongo import MongoClient
from settings import *

class MongoAPI:
    def __init__(self):
        self.client = MongoClient(MONNGODB_URI)  
      
        database = DATABASE_NAME
        collection = COLLECTION_NAME
        cursor = self.client[database]
        self.collection = cursor[collection]

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        new_document = data
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self,data):
        filt = {"celular":data['celular']}
        updated_data = {"$set": data}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output
    
    def delete(self, data):
        filt = data
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output