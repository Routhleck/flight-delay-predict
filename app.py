from flask import Flask, request, jsonify

from API.algorithm import setDepartureAirport, setArriveAirport, delayPredict, getDepartureWeather, getArriveWeather
from API.loginAndRegister import login, deleteUser, judgeAdmin, selectAllUser
from API.loginAndRegister import signup
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


# app.all('*', function(req,res,next){
#
#
# })

@app.route('/')
@cross_origin(supports_credentials=True)
def hello_world():
    return 'hello,world'


# 登陆
@app.route('/login', methods=['post'])
@cross_origin(supports_credentials=True)
def doLogin():
    print("前端发出请求")
    data = request.get_json()
    id = data.get('username')
    password = data.get('password')
    print(id)
    print(password)
    confirm = login(id, password)
    print(confirm)
    if confirm == 'success':
        return 'true'
    else:
        return 'false'


# 注册
@app.route('/signup', methods=['post'])
@cross_origin(supports_credentials=True)
def dosignup():
    data = request.get_json()
    id = data.get('username')
    password = data.get('password')
    print(id)
    print(password)
    confirm = signup(id, password)
    print(confirm)
    return confirm


# 删除
@app.route('/deleteuser')
@cross_origin(supports_credentials=True)
def dodelete():
    data = request.get_json()
    id = data.get('username')
    confirm = deleteUser(id)
    return confirm


# 选择起始机场
@app.route('/setDepartureAirport', methods=['post'])
@cross_origin(supports_credentials=True)
def doSetDepartureAirport():
    data = request.get_json()
    print(data)
    firstair = data.get('showmsg')
    print(firstair)
    setDepartureAirport(firstair)
    return "true"


# # 选择起始机场
# @app.route('/setDepartureAirport/<departureAirport>')
# def doSetDepartureAirport(departureAirport):
#     confirm = setDepartureAirport(departureAirport)
#     return confirm

# 选择到达机场
@app.route('/setArriveAirport', methods=['post'])
@cross_origin(supports_credentials=True)
def doSetArriveAirport(arriveAirport):
    data = request.get_json()
    print(data)
    secondair = data.get('showemsg')
    print(secondair)
    confirm = setArriveAirport(arriveAirport)
    return confirm


# 延误预测
@app.route('/delayPredict')
def doDelayPredict():
    # data = request.get_json()
    # print(data)
    # hour = data.get('hour')
    # print(hour)
    hour = 13
    confirm = delayPredict(hour)
    return confirm


# 获取出发天气
@app.route('/getDepartureWeather')
def doGetDepartureWeather():
    confirm = getDepartureWeather()
    return confirm


# 获取到达天气
@app.route('/getArriveWeather')
def doGetArriveWeather():
    confirm = getArriveWeather()
    return confirm


# 判断权限
@app.route('/judgeAdmin', methods=['post'])
@cross_origin(supports_credentials=True)
def doJudgeAdmin():
    data = request.get_json()
    id = data.get('username')
    confirm = judgeAdmin(id)
    return confirm


# 列出所有用户
@app.route('/listUser', methods=['get'])
@cross_origin(supports_credentials=True)
def listAllUser():
    rs = selectAllUser()
    return str(rs)


if __name__ == '__main__':
    app.run(debug=True)
