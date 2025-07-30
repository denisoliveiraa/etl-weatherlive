from config.db_config import connection as conn

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        latitude TEXT,
        longitude TEXT,
        temperature TEXT,
        time TEXT
    );
""")

cur.execute("INSERT INTO logs (latitude, longitude,temperature, time) VALUES (%s, %s)", ("Ana", 30))

conn.commit()
cur.close()
conn.close()