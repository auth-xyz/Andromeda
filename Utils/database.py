from pymongo import MongoClient


class Database:
    def __init__(self, db_uri, db_name, db_collection):
        self.db_uri = db_uri
        self.db_name = db_name
        self.collection_name = db_collection
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        try:
            self.client = MongoClient(self.db_uri)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
        except Exception as e:
            print(f"[mongo-db.error] : {e}")

    def disconnect(self):
        if self.client:
            self.client.close()

    def insert_document(self, document):
        try:
            result = self.collection.insert_one(document)
            print(f"[mongo-db.output] : Document inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"[mongo-db.error] : inserting document: {e}")

    def find_document(self, query):
        try:
            document = self.collection.find_one(query)
            return document
        except Exception as e:
            print(f"[mongo-db.error] : finding document: {e}")

    def find_all(self, payload):
        try:
            results = {}
            for collection_name in self.db.list_collection_names():
                collection = self.db[collection_name]
                documents = collection.find(payload)
                results[collection_name] = list(documents)
            return results
        except Exception as e:
            print(f"Error finding documents with payload: {e}")

    def update_document(self, query, update_data):
        try:
            result = self.collection.update_one(query, {"$set": update_data})
            print(f"[mongo-db.output] : Document updated: {result.modified_count} document(s) modified")
        except Exception as e:
            print(f"[mongo-db.error] : updating document: {e}")

    def find_in_all(self, query):
        try:
            results = []
            for collection_name in self.client[self.db_name].list_collection_names():
                collection = self.client[self.db_name][collection_name]
                documents = collection.find(query)
                results.extend(list(documents))

            return results
        except Exception as e:
            print(f"Error finding documents across collections: {e}")
