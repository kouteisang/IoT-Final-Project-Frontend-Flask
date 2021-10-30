import json
import re

from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/test_demo", methods=['GET'])
def test_demo():
    id = request.args.get('id')
    print(id)
    return "OK";


@app.route("/getData", methods=['GET'])
def get_data():
    list = []
    for i in range(10):
        list.append({'roomNumber':i,'number':i*10})
    res = json.dumps(list)
    print(res)
    return res

@app.route("/getPhoto", methods=['GET'])
def get_photo():
    roomNumber = int(request.args.get('roomNumber'))
    print(roomNumber)
    return '../static/img/7091635508858_.pic.jpg'

@app.route("/history/<roomNumberParam>")
def history(roomNumberParam):
    print(roomNumberParam)
    return render_template('history.html')

@app.route("/getHistoryData", methods = ['GET'])
def getHistoryData():
    roomNumber = int(request.args.get('roomNumber'))
    list = []
    for i in range(5):
        name = None
        if i == 0:
            name = 'Monday'
        elif i == 1:
            name = 'Tuesday'
        elif i == 2:
            name = 'Wednesday'
        elif i == 3:
            name = 'Thursday'
        elif i == 4:
            name = 'Friday'
        data = [i+1] * 26
        list.append({'name':name,'historyData':data})
    return json.dumps(list)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=False)