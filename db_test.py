'''
 This script contains the code to initialize connections to all of the included
 database servers. To use: comment out the ones you don't need,
 or copy/paste the relevant code to a new script.
'''
import os


def test_postgres():
    import psycopg2
    try:
        conn = psycopg2.connect(
            host="postgres",
            dbname="postgres",
            user="admin",
            password="LocalPasswordOnly"
        )
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS favorite_pokemon;")
        cur.execute(
            "CREATE TABLE favorite_pokemon (id SERIAL PRIMARY KEY, name TEXT);")
        cur.execute(
            "INSERT INTO favorite_pokemon (name) VALUES (%s);", ("Sudowoodo",))
        conn.commit()
        cur.execute("SELECT name FROM favorite_pokemon;")
        print("[PostgreSQL Works!] Favorite Pokémon:", cur.fetchone()[0])
        cur.close()
        conn.close()
    except Exception as e:
        print("[PostgreSQL] Error:", e)


def test_sqlite():
    import sqlite3
    try:
        conn = sqlite3.connect("local.db")
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS favorite_pokemon;")
        cur.execute(
            "CREATE TABLE favorite_pokemon (id INTEGER PRIMARY KEY, name TEXT);")
        cur.execute(
            "INSERT INTO favorite_pokemon (name) VALUES (?);", ("Sudowoodo",))
        conn.commit()
        cur.execute("SELECT name FROM favorite_pokemon;")
        print("[SQLite Works!] Favorite Pokémon:", cur.fetchone()[0])
        cur.close()
        conn.close()
    except Exception as e:
        print("[SQLite] Error:", e)


def test_redis():
    import redis
    try:
        r = redis.Redis(host="redis", port=6379, decode_responses=True)
        r.set("favorite_pokemon", "Sudowoodo")
        name = r.get("favorite_pokemon")
        print("[Redis Works!] Favorite Pokémon:", name)
    except Exception as e:
        print("[Redis] Error:", e)


def test_mongodb():
    from pymongo import MongoClient
    try:
        client = MongoClient("mongodb://mongo:27017/")
        db = client.pokedex
        db.favorite_pokemon.drop()
        db.favorite_pokemon.insert_one({"name": "Sudowoodo"})
        doc = db.favorite_pokemon.find_one({}, {"_id": 0, "name": 1})
        print("[MongoDB Works!] Favorite Pokémon:", doc["name"])
    except Exception as e:
        print("[MongoDB] Error:", e)


def test_cockroach():
    from sqlalchemy import create_engine, text
    try:
        engine = create_engine(
            "cockroachdb://root@cockroach:26257/defaultdb?sslmode=disable")
        with engine.connect() as conn:
            conn.execute(text("DROP TABLE IF EXISTS favorite_pokemon;"))
            conn.execute(
                text("CREATE TABLE favorite_pokemon (id SERIAL PRIMARY KEY, name STRING);"))
            conn.execute(
                text("INSERT INTO favorite_pokemon (name) VALUES ('Sudowoodo');"))
            result = conn.execute(text("SELECT name FROM favorite_pokemon;"))
            print("[CockroachDB Works!] Favorite Pokémon:", result.fetchone()[0])
    except Exception as e:
        print("[CockroachDB] Error:", e)


def test_neo4j():
    from neo4j import GraphDatabase
    try:
        driver = GraphDatabase.driver(
            "bolt://neo4j:7687", auth=("neo4j", "testpassword"))
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            session.run("CREATE (:Pokemon {name: 'Sudowoodo'})")
            result = session.run(
                "MATCH (p:Pokemon) RETURN p.name AS name LIMIT 1")
            print("[Neo4j Works!] Favorite Pokémon:", result.single()["name"])
    except Exception as e:
        print("[Neo4j] Error:", e)


# Run all tests
test_postgres()
test_sqlite()
test_redis()
test_mongodb()
test_cockroach()
test_neo4j()
