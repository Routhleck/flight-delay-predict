from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelTrain.weather_predict.Main_weather_predict import weather_predict_single
from modelTrain.predict.predict_test import predict
# 选择起始机场
def setDepartureAirport(departureAirport):
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
    # 删除selectAirport表中的所有数据
    sql = 'delete from selectAirport'
    session.execute(sql)
    session.commit()
    session.close()
    # 插入起始机场departureAirport到selectAirport表中
    session = Session()
    sql = 'insert into selectAirport(departureId) values("{}")'.format(departureAirport)
    session.execute(sql)
    session.commit()
    session.close()
    print('起始机场已设置为：' + departureAirport)

    # 起始机场天气预测
    isDeparture = True
    weather_predict_single(departureAirport, engine, Session, isDeparture)
    return True

# 选择到达机场
def setArriveAirport(arriveAirport):
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


    # 获取selectAirport表中departureId的第一行
    session = Session()
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]
    session.close()

    # 更新selectAirport表departureId = departureAirport的行的arriveId为arriveAirport
    session = Session()
    sql = 'update selectAirport set arriveId = "{}" where departureId = "{}"'.format(arriveAirport, departureAirport)
    session.execute(sql)
    session.commit()
    session.close()
    print('到达机场已设置为：' + arriveAirport)

    # 到达机场天气预测
    isDeparture = False
    weather_predict_single(departureAirport, engine, Session, isDeparture)
    return True

# 延误预测
def delayPredict():
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

    # 获取selectAirport表中departureId的第一行
    session = Session()
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]

    # 获取airport表中airportId = departureAirport的行的weatherId的一行
    sql = 'select weatherId from airport where airportId = "{}"'.format(departureAirport)
    weatherId = session.execute(sql).fetchone()[0]

    # 获取departureWeather表中的天气
    session = Session()
    sql = 'select * from departureWeather where weatherId = {}'.format(weatherId)
    rs = session.execute(sql).fetchall()
    weatherList = []
    for i in rs:
        weatherList.append(i)
    session.close()

    for i in range(len(weatherList)):
        result_departure, result_arrive = predict(weatherList[i][2:9])
        # 更新departureWeather表中的延误
        session = Session()
        sql = 'update departureweather set delayDeparture = {}, delayArrive = {} where date = {}'.format(result_departure, result_arrive, weatherList[i][1])
        session.execute(sql)
        session.commit()
        session.close()
    print('延误预测完成')
    return True

# 获取出发天气
def getDepartureWeather():
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

    # 获取selectAirport表中departureId的第一行
    session = Session()
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]
    session.close()

    # 获取airport表中airportId = departureAirport的行的weatherId的一行
    session = Session()
    sql = 'select weatherId from airport where airportId = "{}"'.format(departureAirport)
    weatherId = session.execute(sql).fetchone()[0]
    session.close()

    # 获取departureWeather表中的天气
    session = Session()
    sql = 'select * from departureWeather where weatherId = {}'.format(weatherId)
    rs = session.execute(sql).fetchall()
    weatherList = []
    for i in rs:
        weatherList.append(i)
    session.close()
    # 返回天气与延误信息二维列表，形式如：[date, avg_temp, max_temp, min_temp, prec, pressure, wind_direction, wind_speed, delayDeparture, delayArrive]
    return weatherList[0:len(weatherList)-1][1:11]

# 获取到达天气
def getArriveWeather():
    # 配置数据库
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

    # 获取selectAirport表中departureId的第一行
    session = Session()
    sql = 'select departureId from selectAirport limit 1'
    departureAirport = session.execute(sql).fetchone()[0]
    session.close()

    # 获取对应的arriveId
    session = Session()
    sql = 'select arriveId from selectAirport where departureId = "{}"'.format(departureAirport)
    arriveAirport = session.execute(sql).fetchone()[0]

    # 获取airport表中airportId = arriveAirport的行的weatherId的一行
    sql = 'select weatherId from airport where airportId = "{}"'.format(arriveAirport)
    weatherId = session.execute(sql).fetchone()[0]
    session.close()

    # 获取arriveWeather表中的天气
    session = Session()
    sql = 'select * from arriveWeather where weatherId = {}'.format(weatherId)
    rs = session.execute(sql).fetchall()
    weatherList = []
    for i in rs:
        weatherList.append(i)
    session.close()
    # 返回天气信息二维列表，形式如：[date, avg_temp, max_temp, min_temp, prec, pressure, wind_direction, wind_speed]
    return weatherList[0:len(weatherList)-1][1:9]
