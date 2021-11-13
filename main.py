import json
import re
from flask_login import current_user, login_required, LoginManager, UserMixin, login_user
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.secret_key = 'abc'  # 设置表单交互密钥
CORS(app, resources={r'/*': {'origins': '*'}})
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'
login_manager.init_app(app)


class User(UserMixin):
    pass

users = [
    {'id':'1', 'username': 'test', 'password': 'test'},
]
def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user

@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        user = query_user(user_id)
        if user is not None and request.form['password'] == user['password']:
            curr_user = User()
            curr_user.id = user_id
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)
            return redirect(url_for('index'))

    # GET 请求
    return render_template('login.html')


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

@login_required
@app.route("/photo/<roomNumberParam>")
def testPhoto(roomNumberParam):

    # here current_photo is a bytes-like object, just use you read image with "rb"
    return render_template("imgTest.html")

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
        data = [i+1] * 24
        list.append({'name':name,'historyData':data})
    return json.dumps(list)

@app.route("/loginPage")
def loginPage():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=False)