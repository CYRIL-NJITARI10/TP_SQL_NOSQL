import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['DB_NoSQL_1']
collection = db['data']

with open('../data/dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    collection.insert_many(data)

print("Data imported into MongoDB!")
