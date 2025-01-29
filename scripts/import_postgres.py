import csv
import psycopg2
import time

conn = psycopg2.connect(
    dbname="DBR",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
print("Connection to the database successful!")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    Num_Acc TEXT,
    id_usager TEXT,
    id_vehicule TEXT,
    num_veh TEXT,
    place TEXT,
    catu TEXT,
    grav TEXT,
    sexe TEXT,
    an_nais TEXT,
    trajet TEXT,
    secu1 TEXT,
    secu2 TEXT,
    secu3 TEXT,
    locp TEXT,
    actp TEXT,
    etatp TEXT
);
""")
conn.commit()
print("Creation of table data successful!")
start_time = time.time()
with open('../data/usagers-2023.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        if len(row) == 16:
            cursor.execute("""
            INSERT INTO data (
                Num_Acc, id_usager, id_vehicule, num_veh, place, catu, grav, sexe, 
                an_nais, trajet, secu1, secu2, secu3, locp, actp, etatp
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, row)
        else:
            print(f"Skipping row due to incorrect number of columns: {row}")

conn.commit()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Data imported into PostgreSQL in {elapsed_time:.2f} seconds!")

cursor.close()
conn.close()
