from modelTrain.weather_predict.Main_weather_predict import weather_predict_single
from modelTrain.predict.predict_test import predict
from modelTrain.weather_predict.Main_weather_predict import weather_predict_all
import pandas as pd

# 先全部预测天气接着预测延迟
from sql import querySomething, queryAllthing


def predictAll():
    # 预测所有机场近7天的数据
    weather_predict_all()
    # 读取所有机场的天气数据
    airport = pd.read_csv("dataset/airport.csv", encoding='gbk')
    weather_dict = {}
    for i in range(len(airport)):
        weather_dict[airport['机场编码'][i]] = pd.read_csv("weather_predict/weatherData/" + airport['机场编码'][i] + ".csv")

    # 将csv中的天气数据进行预测并将结果加入到csv中
    for city in weather_dict:
        # 新增行
        weather_dict[city]['预测出发延迟'] = float(0)
        weather_dict[city]['预测到达延迟'] = float(0)
        for i in range(len(weather_dict[city])):
            result_departure, result_arive = predict(weather_dict[city].iloc[i][1:8])
            # 添加到第i行末尾
            weather_dict[city].loc[i, '预测出发延迟'] = result_departure
            weather_dict[city].loc[i, '预测到达延迟'] = result_arive
        # 写入csv
        weather_dict[city].to_csv("temp_result/" + city + ".csv")


def predictSingle(airportId, engine, session):
    # 预测单个机场近7天的数据
    weatherId = weather_predict_single(airportId, engine, session)
    a = querySomething(engine, "weatherinfo", weatherId,"weatherId","*")
    weatherList = []
    for row in a:
        weatherList.append(row)

    weather_dict = {airportId: weatherList}

    # 将csv中的天气数据进行预测并将结果加入到csv中
    # 新增行
    for i in range(len(weather_dict[airportId])):
        result_departure, result_arrive = predict(weather_dict[airportId][i][2:9])
        # 添加到第i行末尾

        sql = "update weatherInfo set delayDeparture = " + str(
            result_departure[0]) + ",delayArrive = "+str(result_arrive[0]) +" where date = "+'\''+str(weather_dict[airportId][i][1])+'\''
        session.execute(sql)
        session.commit()
        session.close()

    # 写入csv
    #weather_dict[airportId].to_csv("/temp_result/" + airportId + ".csv")

    # 将csv传入数据库中
    print(weather_dict[airportId])


# predictFromWeatherAll()

'''
airport = pd.read_csv("dataset/airport.csv", encoding= 'gbk')
weather_dict = {}
for i in range(len(airport)):
    weather_dict[airport['机场编码'][i]] = pd.read_csv("weather_predict/weatherData/" + airport['机场编码'][i] + ".csv")
for city in weather_dict:
    print(weather_dict[city].iloc[0])
'''
