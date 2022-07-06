import joblib
import pandas as pd
from sklearn import preprocessing, metrics, svm
# 测试数据
data_test = [2.3,6.7,-2.1,0.0,1024.3,231.0,2.0]
#转换为二维数组
data_test = pd.DataFrame(data_test).T
# 加载模型
model_departure = joblib.load('train/delayDeparture.pkl')
model_arive = joblib.load('train/delayArive.pkl')

# 模型预测
def predict(data):
    # 标准化
    ss_X = preprocessing.StandardScaler()
    data_scaled = ss_X.fit_transform(data)
    data_pred_departure = model_departure.predict(data_scaled)
    data_pred_arrive = model_arive.predict(data_scaled)
    return data_pred_departure, data_pred_arrive
result_departure, result_arive = predict(data_test)
print('出发延迟: ', result_departure, '到达延迟: ', result_arive)