import csv
from cassandra.cluster import Cluster
import uuid
import time

try:
    cluster = Cluster(['cassandra'], port=9042)
    session = cluster.connect()
    print("Connection to the database successful!")
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS DB_NoSQL_2
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)
    print("Creation of the keyspace successful!")
    time.sleep(10)

    session.set_keyspace('db_nosql_2')

    session.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id UUID PRIMARY KEY,
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

    start_time = time.time()

    with open('/app/data/usagers-2023.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 16:
                session.execute("""
                INSERT INTO data (
                    id, Num_Acc, id_usager, id_vehicule, num_veh, place, catu, grav, 
                    sexe, an_nais, trajet, secu1, secu2, secu3, locp, actp, etatp
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (uuid.uuid4(), *row))
            else:
                print(f"Skipping row due to incorrect number of columns: {row}")

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Data imported into Cassandra in {elapsed_time:.2f} seconds!")

except Exception as e:
    print(f"An error occurred: {e}")
