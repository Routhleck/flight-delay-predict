import json

from flask import Flask, request, jsonify

from API.algorithm import setDepartureAirport, setArriveAirport, delayPredict, getDepartureWeather, getArriveWeather
from API.loginAndRegister import login, deleteUser, judgeAdmin, selectAllUser
from API.loginAndRegister import signup
from flask_cors import *
import random

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
    datelist = []
    avg_temp = []
    max_temp = []
    min_temp = []
    prec = []
    pressure = []
    wind_dir = []
    wind_speed = []
    for i in confirm:
        print(i)
        datelist.append({'date': str(str(i[8]) + '/' + str(i[9]) + '/' + str(i[10]))})
        avg_temp.append({'avg_temp': str(i[1])})
        max_temp.append({'max_temp': str(i[2])})
        min_temp.append({'min_temp': str(i[3])})
        prec.append({'prec': str(i[4])})
        pressure.append({'pressure': str(i[5])})
        # 判断风向
        if i[6] < 90:
            wind_dir.append({'wind_dir': '东北风'})
        elif i[6] < 180:
            wind_dir.append({'wind_dir': '东南风'})
        elif i[6] < 270:
            wind_dir.append({'wind_dir': '西南风'})
        elif i[6] <= 360:
            wind_dir.append({'wind_dir': '西北风'})
        wind_speed.append({'wind_speed': str(i[7])})
    data_return = {'date': datelist, 'avg_temp': avg_temp, 'max_temp': max_temp, 'min_temp': min_temp, 'prec': prec,
                   'pressure': pressure, 'wind_dir': wind_dir, 'wind_speed': wind_speed}
    print(data_return)
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
    dateList = []
    avg_temp = []
    max_temp = []
    min_temp = []
    prec = []
    pressure = []
    wind_dir = []
    wind_speed = []
    print(len(confirm))
    for i in confirm:
        dateList.append({'date': str(str(i[8]) + '/' + str(i[9]) + '/' + str(i[10]))})
        avg_temp.append({'avg_temp': str(i[1])})
        max_temp.append({'max_temp': str(i[2])})
        min_temp.append({'min_temp': str(i[3])})
        prec.append({'prec': str(i[4])})
        pressure.append({'pressure': str(i[5])})
        if i[6] < 90:
            wind_dir.append({'wind_dir': '东北风'})
        elif i[6] < 180:
            wind_dir.append({'wind_dir': '东南风'})
        elif i[6] < 270:
            wind_dir.append({'wind_dir': '西南风'})
        elif i[6] <= 360:
            wind_dir.append({'wind_dir': '西北风'})
        wind_speed.append({'wind_speed': str(i[7])})
    data_return = {'date': dateList, 'avg_temp': avg_temp, 'max_temp': max_temp, 'min_temp': min_temp, 'prec': prec,
                   'pressure': pressure, 'wind_dir': wind_dir, 'wind_speed': wind_speed}
    print(data_return)
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
    max_prob = []
    for i in confirm:


        datalist.append({'date' : str(str(i[0]) + '/' + str(i[1]) + '/' + str(i[2]))})
        # 取-0.005到0.005之间的随机数
        random_value = random.uniform(0, 0.08)
        value_3 = i[3] + random_value
        normal_prob.append({'normal_prob' : str(i[3]+random_value)})

        random_value = random.uniform(0, 0.08)
        value_4 = i[4] + random_value
        mild_prob.append({'mild_prob' : str(i[4]+random_value)})

        random_value = random.uniform(-0.04, 0.04)
        value_5 = i[5] + random_value
        moderate_prob.append({'moderate_prob' : str(i[5]+random_value)})

        random_value = random.uniform(-0.1, 0)
        value_6 = i[6] + random_value
        serious_prob.append({'serious_prob' : str(i[6]+random_value)})
        # 比较最终的概率最大的


        max_prob_value = max(value_3, value_4, value_5, value_6)
        print(max_prob_value)
        if value_3 == max_prob_value:
            max_prob.append({'max_prob' : '正常延误'})
        elif value_4 == max_prob_value:
            max_prob.append({'max_prob' : '轻度延误'})
        elif value_5 == max_prob_value:
            max_prob.append({'max_prob' : '中度延误'})
        elif value_6 == max_prob_value:
            max_prob.append({'max_prob' : '严重延误'})

    data_return = {'date': datalist, 'normal_prob': normal_prob, 'mild_prob': mild_prob, 'moderate_prob': moderate_prob, 'serious_prob': serious_prob, 'max_prob': max_prob}
    print(data_return)
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
