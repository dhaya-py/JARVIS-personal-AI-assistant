import sqlite3
from datetime import datetime

conn = sqlite3.connect("jarvis.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT,
    response TEXT,
    timestamp TEXT
)
""")

def log_interaction(command, response):
    cursor.execute(
        "INSERT INTO logs (command, response, timestamp) VALUES (?, ?, ?)",
        (command, response, datetime.now().isoformat())
    )
    conn.commit()
