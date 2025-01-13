import csv
import psycopg2

conn = psycopg2.connect(
    dbname="DBR",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    column1 TEXT,
    column2 TEXT,
    column3 TEXT
);
""")

conn.commit()

with open('../data/dataset.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO data (column1, column2, column3) VALUES (%s, %s, %s);",
            row
        )
conn.commit()
cursor.close()
conn.close()
