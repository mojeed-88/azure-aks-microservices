import os
import time
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "shoestore")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=5
    )

def wait_for_db(retries=10, delay=5):
    for _ in range(retries):
        try:
            conn = get_connection()
            conn.close()
            return
        except Exception:
            time.sleep(delay)
    raise Exception("Database not ready")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    ...
    conn.commit()
    cur.close()
    conn.close()

@app.route("/health")
def health():
    try:
        conn = get_connection()
        conn.close()
        return jsonify({"status": "ok"}), 200
    except Exception:
        return jsonify({"status": "db-down"}), 500

if __name__ == "__main__":
    wait_for_db()
    init_db()
    app.run(host="0.0.0.0", port=5000)

