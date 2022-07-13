from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelTrain.weather_predict.Main_weather_predict import weather_predict_single
from modelTrain.predict.useModel import predict
from math import radians, cos, sin, asin, sqrt

# 配置数据库
hostname = '8.141.236.100'
port = '3306'
database = 'db01'
username = 'heyi'
pwd = 'HeYi1456'
dburl = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(username, pwd, hostname, port, database)
# 创建数据库连接对象
engine = create_engine(dburl, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# 辅助函数,用于其他函数的实现
def geoDistance(lat1, lon1, lat2, lon2):
    # 将十进制度数转化为弧度
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


# 选择起始机场
def setDepartureAirport(departureAirport):

    # 删除selectAirport表中的所有数据
    sql = 'delete from selectAirport'
    session.execute(sql)
    session.commit()
    # 插入起始机场departureAirport到selectAirport表中
    sql = 'insert into selectAirport(departureId) values("{}")'.format(departureAirport)
    session.execute(sql)
    session.commit()
    session.close()
    print('起始机场已设置为：' + departureAirport)

    # 起始机场天气预测
    isDeparture = True
    weather_predict_single(departureAirport, engine, session, isDeparture)
    return "true"

# 选择到达机场
def setArriveAirport(arriveAirport):


    # 获取selectAirport表中departureId的第一行
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]
    # session.close()

    # 更新selectAirport表departureId = departureAirport的行的arriveId为arriveAirport
    sql = 'update selectAirport set arriveId = "{}" where departureId = "{}"'.format(arriveAirport, departureAirport)
    session.execute(sql)
    session.commit()
    print('到达机场已设置为：' + arriveAirport)

    # 到达机场天气预测
    isDeparture = False
    weather_predict_single(departureAirport, engine, session, isDeparture)
    return "true"

# 延误预测
def delayPredict(hour):
    # 获取selectAirport表中departureId的第一行
    global session
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]

    # 获取selectAirport表中arriveId的第一行
    sql = 'select arriveId from selectAirport limit 1'
    arriveAirport = session.execute(sql).fetchone()[0]

    # 获取airline表中的随机一行的id
    sql = 'select id from airline order by RAND() limit 1'
    # 随机获取一行
    airlineId = session.execute(sql).fetchone()[0]

    # 获取airport表中airportId = departureAirport的行的weatherId的一行
    sql = 'select weatherId from airport where airportId = "{}"'.format(departureAirport)
    weatherId = session.execute(sql).fetchone()[0]

    # 获取airport表中airportId = departureAirport和arriveAirport的行的longitude和latitude
    sql = 'select longitude, latitude from airport where airportId = "{}"'.format(departureAirport)
    departure_longitude = session.execute(sql).fetchone()[0]
    departure_latitude = session.execute(sql).fetchone()[1]
    sql = 'select longitude, latitude from airport where airportId = "{}"'.format(arriveAirport)
    print(arriveAirport)
    arrive_longitude = session.execute(sql).fetchone()[0]
    arrive_latitude = session.execute(sql).fetchone()[1]
    length = geoDistance(departure_longitude, departure_latitude, arrive_longitude, arrive_latitude)

    # 获取departureWeather表中的天气
    sql = 'select * from departureWeather where weatherId = {}'.format(weatherId)
    rs = session.execute(sql).fetchall()
    weatherList = []
    for i in rs:
        weatherList.append(i)

    for i in range(len(weatherList)):
        # 将departureId,arrivalId,airlineId,length和hour加入到列表中创建为新的list
        newList = [departureAirport, arriveAirport, airlineId, length, weatherList[i][1], weatherList[i][2], weatherList[i][3], weatherList[i][4], weatherList[i][5],
                    weatherList[i][6], weatherList[i][7], weatherList[i][8], weatherList[i][9], weatherList[i][10], hour]

        pred = predict(newList)
        # 更新departureWeather表中的延误
        session = Session()
        sql = 'update departureweather set normal_prob = {}, mild_prob = {}, moderate_prob = {}, serious_prob = {} where year = {} and month = {} and day = {}'.format(pred[0], pred[1], pred[2], pred[3], weatherList[i][8], weatherList[i][9], weatherList[i][10])
        session.execute(sql)
        session.commit()
    print('延误预测完成')
    # 获取departureWeather表中的normal_prob, mild_prob, moderate_prob, serious_prob
    sql = 'select normal_prob, mild_prob, moderate_prob, serious_prob from departureWeather'
    rs = session.execute(sql).fetchall()
    pred = []
    for i in rs:
        pred.append(i)
    session.close()
    return str(pred)

# 获取出发天气
def getDepartureWeather():

    # 获取selectAirport表中departureId的第一行
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]

    # 获取airport表中airportId = departureAirport的行的weatherId的一行
    sql = 'select weatherId from airport where airportId = "{}"'.format(departureAirport)
    weatherId = session.execute(sql).fetchone()[0]

    # 获取departureWeather表中的天气
    sql = 'select * from departureWeather where weatherId = {}'.format(weatherId)
    rs = session.execute(sql).fetchall()
    weatherList = []
    for i in rs:
        weatherList.append(i)
    session.close()
    # 返回天气与延误信息二维列表，形式如：[avg_temp, max_temp, min_temp, prec, pressure, wind_direction, wind_speed, year, month, day]
    return str(weatherList[0:len(weatherList)-1][1:11])

# 获取到达天气
def getArriveWeather():
    # 获取selectAirport表中departureId的第一行
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]

    # 获取对应的arriveId
    sql = 'select arriveId from selectAirport where departureId = "{}"'.format(departureAirport)
    arriveAirport = session.execute(sql).fetchone()[0]

    # 获取airport表中airportId = arriveAirport的行的weatherId的一行
    sql = 'select weatherId from airport where airportId = "{}"'.format(arriveAirport)
    weatherId = session.execute(sql).fetchone()[0]

    # 获取arriveWeather表中的天气
    sql = 'select * from arriveWeather where weatherId = {}'.format(weatherId)
    rs = session.execute(sql).fetchall()
    weatherList = []
    for i in rs:
        weatherList.append(i)
    session.close()
    # 返回天气信息二维列表，形式如：[avg_temp, max_temp, min_temp, prec, pressure, wind_direction, wind_speed, year, month, day]
    return str(weatherList[0:len(weatherList)-1][1:11])