from flask import Flask, request, jsonify

from API.algorithm import setDepartureAirport, setArriveAirport, delayPredict, getDepartureWeather, getArriveWeather
from API.loginAndRegister import login, deleteUser
from API.loginAndRegister import signup
from flask_cors import *


# def after_request(response):
#     response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or 'http://127.0.0.1:8080'
#     response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,Accept,Origin,Referer,User-Agent'
#     response.headers['Access-Control-Allow-Credentials'] = 'true'
#     return response


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
    return 'true'
    # if confirm == 'success':
    #     return 'true'
    # else:
    #     return 'false'


# 注册
@app.route('/signup/<id>/<password>', methods=['get'])
def dosignup(id, password):
    confirm = signup(id, password)
    return confirm


# 删除
@app.route('/deleteuser/<userid>')
def dodelete(userid):
    confirm = deleteUser(userid)
    return confirm


# 选择起始机场
@app.route('/setDepartureAirport/<departureAirport>')
def doSetDepartureAirport(departureAirport):
    confirm = setDepartureAirport(departureAirport)
    return confirm


# 选择到达机场
@app.route('/setArriveAirport/<arriveAirport>')
def doSetArriveAirport(arriveAirport):
    confirm = setArriveAirport(arriveAirport)
    return confirm


# 延误预测
@app.route('/delayPredict/<arriveAirport>')
def doDelayPredict(arriveAirport):
    confirm = delayPredict()
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


if __name__ == '__main__':
    app.run(debug=True)