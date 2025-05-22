import os
import certifi
import pandas as pd
import numpy as np

import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv('MONGO_DB_URI')

# print(MONGO_DB_URI)
ca = certifi.where()


class ExtractNetworkData():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def file_type_converter(self,file_path):
        try:
            data=pd.read_csv('Network_Data/phishing_dataset.csv')
            data.reset_index(drop=True,inplace=True)

            # Converting the data in key:value pairs in Json format and storing them to MongoDB server.
            records=list(json.loads(data.T.to_json()).values())

            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection = collection
            self.records = records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URI)
            self.database=self.mongo_client[self.database]
            self.collection =self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)   
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__=='__main__':
    FILE_PATH='Network_Data/phishing_dataset.csv'
    DATABASE='dg24'
    Collection='NetworkData'
    networkobj=ExtractNetworkData()
    records=networkobj.file_type_converter(file_path=FILE_PATH)
    print(records)
    num_of_records=networkobj.insert_data_to_mongodb(records,DATABASE,Collection)

    print(num_of_records)


