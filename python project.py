def init_db():
     conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

from flask import Flask, request, jsonify
import requests
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "PUT_YOUR_WEBHOOK_HERE"

def send_to_discord(text):
    data = {
        "content": text
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)

def save_message(text):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            timestamp TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO messages (text, timestamp) VALUES (?, ?)",
        (text, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    send_to_discord(text)
    save_message(text)

    return jsonify({"message": "Message sent successfully!"})

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("SELECT text, timestamp FROM messages")
    rows = cursor.fetchall()

    conn.close()

    time_limit = datetime.now() - timedelta(minutes=30)

    recent_messages = []

    for text, timestamp in rows:
        if datetime.fromisoformat(timestamp) > time_limit:
            recent_messages.append({
                "text": text,
                "time": timestamp
            })

    return jsonify(recent_messages)

if __name__ == '__main__':
    app.run(debug=True)