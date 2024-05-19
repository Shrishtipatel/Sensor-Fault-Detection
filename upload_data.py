from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://shrishtiptl12:shrishtiptl12@cluster0.3zjbouk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="Shrishti"
COLLECTION_NAME="waferfault"


#read data as a DataFrame
df=pd.read_csv("C:\Users\shris\OneDrive\Desktop\Sensor-Fault-Detection\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
df.T
df.T.to_json
df.T.to_json()
json.loads(df.T.to_json())
json.loads(df.T.to_json()).values()
list(json.loads(df.T.to_json()).values())
json_record=list(json.loads(df.T.to_json()).values())

#now dump  the data
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)