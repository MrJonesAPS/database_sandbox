'''
 This script contains the code to initialize connections to all of the included
 database servers. To use: comment out the ones you don't need,
 or copy/paste the relevant code to a new script.
'''

import sqlite3
import redis
from pymongo import MongoClient
import psycopg2

# --- PostgreSQL ---
conn = psycopg2.connect(
    host="postgres", user="admin", password="LocalPasswordOnly", dbname="postgres"
)
print("Connected to PostgreSQL:", conn.get_dsn_parameters())

# --- MongoDB ---
client = MongoClient("mongodb://mongo:27017/")
print("MongoDB databases:", client.list_database_names())

# --- Redis ---
r = redis.Redis(host="redis", port=6379)
r.set("test", "hello")
print("Redis value for 'test':", r.get("test"))

# --- SQLite ---
conn = sqlite3.connect("local.db")
print("Connected to SQLite, cursor:", conn.cursor())