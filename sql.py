from flask import Flask, request, render_template

'''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from modelTrain.delay_predict import predictSingle
'''

app = Flask(__name__)
'''
# 定义数据库属性
hostname = '8.141.236.100'
port = '3306'
database = 'healthcard'
username = 'heyi'
pwd = 'HeYi1456'
dburl = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(username, pwd, hostname, port, database)
# 创建数据库连接对象
engine = create_engine(dburl, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
session.execute("insert into user values ('20301042','123456','1')")
session.commit()
session.close()


with engine.connect() as con:
    idNum = 140203200102083212
    sql = 'select * from peopletb '  # where idCard = '+str(idNum)
    rs = con.execute(sql)
    for row in rs:
        print(row[1])
'''

def querySomething(engine, table, condition, conditionColumn, resultColumn):
    with engine.connect() as con:
        sql = 'select ' + str(resultColumn) + ' from ' + str(table) + ' where ' + str(conditionColumn) + ' = ' + str(condition)
        rs = con.execute(sql)
        return rs

def queryAllthing(engine, table, resultColumn):
    with engine.connect() as con:
        sql = 'select ' + str(resultColumn) + 'from ' + str(table)
        rs = con.execute(sql)
        return rs


