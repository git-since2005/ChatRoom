from flask import Flask, render_template, jsonify, make_response, request
from flask_socketio import SocketIO, send
from bson import ObjectId


from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://abhishek_patil:lHQCzoP3pfCgjKg0@cluster0.ry8d81v.mongodb.net/TestLibrary')
db = client['mydatabase']
collection = db['mycollection']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    records = [i for i in collection.find({})]
    for i in records:
        i['_id'] = str(i['_id'])
    # print(records)
    return make_response(jsonify(records))
    # return make_response([i for i in collection.find({})])
    # return make_response(jsonify({"name":"Abhishek", "age":18}))

def addmsg(msg, tim):
    collection.insert_one({'msg':msg, 'time':tim})
    print("Now!!")
    return "INSERTED!!!"
@socketio.on('message')
def handle_message(msg, time):
    print(f"Message: {msg}")
    send(msg, broadcast=True)
    addmsg(msg, time)

if __name__ == '__main__':
    socketio.run(app, debug=True)