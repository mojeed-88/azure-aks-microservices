from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/message")
def get_message():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT content FROM messages LIMIT 1;")
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return jsonify({"message": row[0]})
        else:
            return jsonify({"message": "No data found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

