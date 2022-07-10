import joblib
import datetime as DT
from modelTrain.weather_predict.GetModel import GetModel
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pandas as pd
import csv
import time

from sql import querySomething


def weather_predict_all():
    airport = pd.read_csv('dataset/airport.csv', encoding='gbk')
    airport_dict = {}
    for i in range(len(airport)):
        airport_dict[airport['机场编码'][i]] = airport['网站ID'][i]
    load = 0
    for city in airport['机场编码']:
        # 训练并保存模型并返回MAE
        r = GetModel(city=city, id=airport_dict[city])
        print("MAE:", r[0])
        # 读取保存的模型
        model = joblib.load('weather_predict/Model.pkl')
        # 最终预测结果
        preds = model.predict(r[1])

        # 将temp存储为csv文件
        # 创建文件对象
        c = 'weather_predict/weatherData/' + city + '.csv'
        f = open(c, 'w', encoding='utf-8', newline='')
        # 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        # 写入表头
        csv_writer.writerow(['日期', '平均气温', '最高气温', '最低气温', '降雨量', '气压', '风向', '风速'])

        # 打印结果到控制台
        print("未来7天预测")
        all_ave_t = []
        all_high_t = []
        all_low_t = []
        all_rainfall = []
        all_pressure = []
        all_wind = []
        all_windSpeed = []
        for a in range(1, 8):
            today = DT.datetime.now()
            time_now = (today + DT.timedelta(days=a)).date()
            csv_writer.writerow(
                [time_now, preds[a][0], preds[a][1], preds[a][2], preds[a][3], preds[a][4], preds[a][5], preds[a][6]])
            print(time_now.year, '/', time_now.month, '/', time_now.day,
                  ': 平均气温', round(preds[a][0], 2), '℃ ',
                  '最高气温', round(preds[a][1], 2), '℃ ',
                  '最低气温', round(preds[a][2], 2), '℃ ',
                  "降雨量", round(preds[a][3], 2), "mm ",
                  '气压', round(preds[a][4], 2), 'hPa ', end=''
                  )
            if preds[a][5] < 90:
                print('东北风', round(preds[a][5], 2), '° ', end='')
            elif preds[a][5] < 180:
                print('东南风', round(preds[a][5], 2), '° ', end='')
            elif preds[a][5] < 270:
                print('西南风', round(preds[a][5], 2), '° ', end='')
            elif preds[a][5] < 360:
                print('西北风', round(preds[a][5], 2), '° ', end='')
            print('风速', round(preds[a][6], 2), 'km/h', )
            all_ave_t.append(preds[a][0])
            all_high_t.append(preds[a][1])
            all_low_t.append(preds[a][2])
            all_rainfall.append(preds[a][3])
            all_pressure.append(preds[a][4])
            all_wind.append(preds[a][5])
            all_windSpeed.append(preds[a][6])

        # 保存csv文件
        f.close()
        load += 1
        if load % 10 == 9:
            time.sleep(6)


def weather_predict_single(airportId, engine, session, isDeparture):
    # airport = pd.read_csv('dataset/airport.csv', encoding='gbk')
    # 从数据库中读airportId,网站ID
    airportId1 ='\''+str(airportId)+'\''
    result = querySomething(engine, "airport", airportId1, "airportId", "weatherId")
    for row in result:
        weatherId = row[0]

    airport_dict = {}
    airport_dict[airportId] = weatherId
    # 训练并保存模型并返回MAE
    r = GetModel(city=airportId, id=airport_dict[airportId])
    print("MAE:", r[0])
    # 读取保存的模型
    model = joblib.load('modelTrain/weather_predict/Model.pkl')
    # 最终预测结果
    preds = model.predict(r[1])

    # 将temp存储为csv文件
    # 创建文件对象

    # 打印结果到控制台
    print("未来7天预测")
    all_ave_t = []
    all_high_t = []
    all_low_t = []
    all_rainfall = []
    all_pressure = []
    all_wind = []
    all_windSpeed = []
    for a in range(1, 8):
        today = DT.datetime.now()
        time_now = (today + DT.timedelta(days=a)).strftime('%Y-%m-%d')
        # csv_writer.writerow(
        value = str(airport_dict[airportId]) + ', \' ' + str(time_now) + ' \' ,' + str(preds[a][0]) + ',' + str(
            preds[a][1]) + ',' + str(preds[a][2]) + ',' + str(preds[a][3]) + ',' + str(preds[a][4]) + ',' + str(
            preds[a][5]) + ',' + str(preds[a][6]) + ',' + str(time_now).split('-')[0] + ',' + str(time_now).split('-')[1] + ',' + str(time_now).split('-')[2] + ',' + '0'
        if isDeparture == True:
            # 删除departureWeather表中的所有数据
            sql = "DELETE FROM departureWeather"
            session.execute(sql)
            session.commit()
            session.close()
            sql = "insert into departureWeather values ({})".format(value)
            session.execute(sql)
            session.commit()
            session.close()
        else:
            # 删除arrivalWeather表中的所有数据
            sql = "DELETE FROM arrivalWeather"
            session.execute(sql)
            session.commit()
            session.close()
            sql = "insert into arriveWeather values ({})".format(value)
            session.execute(sql)
            session.commit()
            session.close()

        print(time_now.year, '/', time_now.month, '/', time_now.day,
              ': 平均气温', round(preds[a][0], 2), '℃ ',
              '最高气温', round(preds[a][1], 2), '℃ ',
              '最低气温', round(preds[a][2], 2), '℃ ',
              "降雨量", round(preds[a][3], 2), "mm ",
              '气压', round(preds[a][4], 2), 'hPa ', end=''
              )
        if preds[a][5] < 90:
            print('东北风', round(preds[a][5], 2), '° ', end='')
        elif preds[a][5] < 180:
            print('东南风', round(preds[a][5], 2), '° ', end='')
        elif preds[a][5] < 270:
            print('西南风', round(preds[a][5], 2), '° ', end='')
        elif preds[a][5] < 360:
            print('西北风', round(preds[a][5], 2), '° ', end='')
        print('风速', round(preds[a][6], 2), 'km/h', )
        all_ave_t.append(preds[a][0])
        all_high_t.append(preds[a][1])
        all_low_t.append(preds[a][2])
        all_rainfall.append(preds[a][3])
        all_pressure.append(preds[a][4])
        all_wind.append(preds[a][5])
        all_windSpeed.append(preds[a][6])
    return weatherId


'''
    temp = {"ave_t": all_ave_t, "high_t": all_high_t, "low_t": all_low_t, "rainfall": all_rainfall, "pressure": all_pressure, "windSpeed": all_windSpeed}


    # 绘画折线图
    plt.plot(range(1, 7), temp["ave_t"], color="green", label="ave_t")
    plt.plot(range(1, 7), temp["high_t"], color="red", label="high_t")
    plt.plot(range(1, 7), temp["low_t"], color="blue", label="low_t")
    plt.legend()  # 显示图例
    plt.ylabel("Temperature(°C)")
    plt.xlabel("day")
    plt.show()
    #降雨量显示
    plt.plot(range(1, 7), temp["rainfall"], color="black", label="rainfall")
    plt.legend()
    plt.ylabel("mm")
    plt.xlabel("day")
    plt.show()
    #气压显示
    plt.plot(range(1, 7), temp["pressure"], color="black", label="pressure")
    plt.legend()
    plt.ylabel("hPa")
    plt.xlabel("day")
    plt.show()
    #风速显示
    plt.plot(range(1, 7), temp["windSpeed"], color="black", label="windSpeed")
    plt.legend()
    plt.ylabel("km/h")
    plt.xlabel("day")
    plt.show()
'''
