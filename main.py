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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('127.0.0.1', port=8080)