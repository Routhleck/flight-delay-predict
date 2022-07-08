from flask import Flask, request, render_template

from API.algorithm import setDepartureAirport, setArriveAirport, delayPredict, getDepartureWeather, getArriveWeather
from API.loginAndRegister import login, deleteUser
from API.loginAndRegister import signup

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello,world'


# 登陆
@app.route('/login/<id>/<password>', methods=['get', 'get'])
def doLogin(id, password):
    confirm = login(id, password)
    return confirm


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
    app.run()
