from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelTrain.delay_predict import predictSingle


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

predictSingle('JDZ',engine=engine,session=session)