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
    for i in range(4):
        list.append({'roomNumber':i,'number':i*10})
    res = json.dumps(list)
    print(res)
    return res

@app.route("/getPhoto", methods=['GET'])
def get_photo():
    roomNumber = int(request.args.get('roomNumber'))
    print(roomNumber)
    if roomNumber == 1:
        return '../static/img/logo.jpg'
    elif roomNumber == 2:
        return '../static/img/7091635508858_.pic.jpg'
    return "OK"




@app.route("/history")
def history():
    return render_template('history.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=False)