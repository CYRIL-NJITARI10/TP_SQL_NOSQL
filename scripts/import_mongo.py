import csv
from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
print("Connection to the database successful!")
db = client['DB_NoSQL_1']
collection = db['data']
print("Creation of the collection successful!")
start_time = time.time()

with open('../data/usagers-2023.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    collection.insert_many(data)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Data imported into MongoDB in {elapsed_time:.2f} seconds!")
