from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 配置数据库
from sql import querySomething, queryAllthing

hostname = '8.141.236.100'
port = '3306'
database = 'db01'
username = 'heyi'
pwd = 'HeYi1456'
dburl = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(username, pwd, hostname, port, database)

# 创建engine和session
engine = create_engine(dburl, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# 登陆接口
def login(idNum, password):
    truepassword = ''
    rs1 = querySomething(engine, 'user', idNum, "userId", "*")
    if rs1 is None:
        return 'flase'
    else:
        rs2 = querySomething(engine, 'user', idNum, "userId", "password")
        for row in rs2:
             truepassword = str(row[0])

    if password == truepassword:
        return 'true'
    else:
        return 'false'


# 注册接口
def signup(id,password):
    sql = "insert into user values ({},{},0)".format(id,password)
    session.execute(sql)
    session.commit()
    session.close()
    return "true"

# 删除接口
def deleteUser(userid):
    sql = "delete from user where userId = {}".format(str(userid))
    session.execute(sql)
    session.commit()
    session.close()
    return "true"

# 判断权限接口
def judgeAdmin(idNum):
    global isAdmin
    rs = querySomething(engine, 'user', idNum, "userId", "isAdmin")
    for row in rs:
        isAdmin = str(row[0])

    if isAdmin == '1':
        return "true"
    else:
        return "false"

# 人员查询
def selectAllUser():
    rs = queryAllthing(engine, 'user', 'userId')
    allUser = []
    for row in rs:
        allUser.append(row[0])

    print(allUser)
    return allUser


