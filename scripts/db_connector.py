import os
import psycopg2
import  json

os.chdir("..")

with open ("scripts/credentials.json", "r", encoding="utf-8") as file:
    credentials = json.load(file)

def get_db_engine():
    db_host = credentials["db_host"]
    db_name = credentials["db_name"]
    db_user = credentials["db_user"]
    db_password = credentials["db_password"]

    conn = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    return conn