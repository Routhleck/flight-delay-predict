import json

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
    id = '\''+str(data.get('username'))+'\''
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
    id = '\'' + str(data.get('username'))+ '\''
    password = data.get('password')
    print(id)
    print(password)
    confirm = signup(id, password)
    print(confirm)
    return confirm


# 删除
@app.route('/deleteuser', methods=['post'])
@cross_origin(supports_credentials=True)
def dodelete():
    data = request.get_json()
    id = '\'' + str(data.get('username'))+ '\''
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
    confirm = setDepartureAirport(firstair)
    datalist = []
    avg_temp = []
    max_temp = []
    min_temp = []
    prec = []
    pressure = []
    wind_dir = []
    wind_speed = []
    for i in confirm:
        datalist.append({'date': str(str(i[8]) + '/' + str(i[9]) + '/' + str(i[10]))})
        avg_temp.append({'avg_temp': str(i[1])})
        max_temp.append({'max_temp': str(i[2])})
        min_temp.append({'min_temp': str(i[3])})
        prec.append({'prec': str(i[4])})
        pressure.append({'pressure': str(i[5])})
        wind_dir.append({'wind_dir': str(i[6])})
        wind_speed.append({'wind_speed': str(i[7])})
    data_return = {'data': datalist, 'avg_temp': avg_temp, 'max_temp': max_temp, 'min_temp': min_temp, 'prec': prec,
                   'pressure': pressure, 'wind_dir': wind_dir, 'wind_speed': wind_speed}
    return jsonify(data_return)


# # 选择起始机场
# @app.route('/setDepartureAirport/<departureAirport>')
# def doSetDepartureAirport(departureAirport):
#     confirm = setDepartureAirport(departureAirport)
#     return confirm

# 选择到达机场
@app.route('/setArriveAirport', methods=['post'])
@cross_origin(supports_credentials=True)
def doSetArriveAirport():
    data = request.get_json()
    print(data)
    secondair = data.get('showemsg')
    print(secondair)
    confirm = setArriveAirport(secondair)
    datalist = []
    avg_temp = []
    max_temp = []
    min_temp = []
    prec = []
    pressure = []
    wind_dir = []
    wind_speed = []
    for i in confirm:
        datalist.append({'date': str(str(i[8]) + '/' + str(i[9]) + '/' + str(i[10]))})
        avg_temp.append({'avg_temp': str(i[1])})
        max_temp.append({'max_temp': str(i[2])})
        min_temp.append({'min_temp': str(i[3])})
        prec.append({'prec': str(i[4])})
        pressure.append({'pressure': str(i[5])})
        wind_dir.append({'wind_dir': str(i[6])})
        wind_speed.append({'wind_speed': str(i[7])})
    data_return = {'data': datalist, 'avg_temp': avg_temp, 'max_temp': max_temp, 'min_temp': min_temp, 'prec': prec,
                   'pressure': pressure, 'wind_dir': wind_dir, 'wind_speed': wind_speed}
    return jsonify(data_return)


# 延误预测
@app.route('/delayPredict', methods=['post'])
@cross_origin(supports_credentials=True)
def doDelayPredict():
    # data = request.get_json()
    # print(data)
    # hour = data.get('hour')
    # print(hour)
    data = request.get_json()
    print(data)
    hourString = data.get('value1')
    hourString = hourString[0:2]
    hour = int(hourString)
    confirm = delayPredict(hour)
    datalist = []
    normal_prob = []
    mild_prob = []
    moderate_prob = []
    serious_prob = []
    for i in confirm:
        datalist.append({'date': str(str(i[0]) + '/' + str(i[1]) + '/' + str(i[2]))})
        normal_prob.append({'normal_prob':str(i[3])})
        mild_prob.append({'mild_prob':str(i[4])})
        moderate_prob.append({'moderate_prob':str(i[5])})
        serious_prob.append({'serious_prob':str(i[6])})
    data_return = {'date': datalist, 'normal_prob': normal_prob, 'mild_prob': mild_prob, 'moderate_prob': moderate_prob, 'serious_prob': serious_prob}
    return jsonify(data_return)


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
    id = '\'' + str(data.get('username'))+ '\''
    confirm = judgeAdmin(id)
    return confirm


# 列出所有用户
@app.route('/listUser', methods=['get'])
@cross_origin(supports_credentials=True)
def listAllUser():
    rs = selectAllUser()
    id_dict = []
    for i in rs:
        id_dict.append({'username': i})
    data = {'users': id_dict}
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
