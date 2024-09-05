from flask import Flask, render_template
from flask_socketio import SocketIO, send

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('')
db = client['mydatabase']
collection = db['mycollection']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)