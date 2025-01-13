import csv
from cassandra.cluster import Cluster
import uuid
import time

try:
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    print("Connection successful!")
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS DB_NoSQL_2
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)
    print("Creation successful!")
    time.sleep(10)


    session.set_keyspace('db_nosql_2')

    session.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id UUID PRIMARY KEY,
        column1 TEXT,
        column2 TEXT,
        column3 TEXT
    );
    """)

    with open('../data/dataset.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            session.execute("""
            INSERT INTO data (id, column1, column2, column3) VALUES (%s, %s, %s, %s);
            """, (uuid.uuid4(), *row))

    print("Data imported into Cassandra!")

except Exception as e:
    print(f"An error occurred: {e}")
