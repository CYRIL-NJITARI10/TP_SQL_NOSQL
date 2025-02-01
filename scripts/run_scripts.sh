#!/bin/bash
python /app/import_mongo.py
python /app/import_cassandra.py
python /app/import_postgres.py