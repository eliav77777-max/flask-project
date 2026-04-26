from flask import Flask, render_template, request, jsonify
from discord_webhook import DiscordWebhook
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

conn = sqlite3.connect('messages.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    timestamp TEXT
)
''')
conn.commit()
discord_webhook_url = 'https://discord.com/api/webhooks/1490802638319648819/FKzZZi1xQdciOFM6OXsQToO_DGUKSlA2GM6jts4i1P72IQ_zVOjYc628WSvs-Jx6RX-3'

def send_to_discord(text):
    webhook = DiscordWebhook(url=discord_webhook_url, content=text)
    webhook.execute()

def save_to_database(text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        "INSERT INTO messages (content, timestamp) VALUES (?, ?)",
        (text, timestamp)
    )
    conn.commit()

@app.route('/input_text', methods=['POST'])
def input_text():
    try:
        if request.is_json:
            data = request.get_json()
            text = data.get('text')
        else:
            text = request.form.get('text')

        if not text:
            return jsonify({"status": "error", "message": "No text provided"})

        send_to_discord(text)
        save_to_database(text)

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        cutoff_time = datetime.now() - timedelta(minutes=30)
        cursor.execute("SELECT content, timestamp FROM messages")
        all_messages = cursor.fetchall()

        recent_messages = []
        for msg in all_messages:
            msg_time = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S')
            if msg_time >= cutoff_time:
                recent_messages.append(msg)

        return jsonify({"status": "success", "messages": recent_messages})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)