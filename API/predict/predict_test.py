import joblib
import pandas as pd
from sklearn import preprocessing, metrics, svm

# 测试数据
# data_test = [2.3,6.7,-2.1,0.0,1024.3,231.0,2.0]
#转换为二维数组
# 模型预测
def predict(data):
    # 加载模型
    model_departure = joblib.load('train/delayDeparture.pkl')
    model_arive = joblib.load('train/delayArive.pkl')
    # 标准化
    ss_X = preprocessing.StandardScaler()
    data = pd.DataFrame(data).T
    data_scaled = ss_X.fit_transform(data)
    data_pred_departure = model_departure.predict(data_scaled)
    data_pred_arrive = model_arive.predict(data_scaled)
    # 反归一化
    data_pred_departure = data_pred_departure * ss_X.scale_[0] + ss_X.mean_[0]
    data_pred_arrive = data_pred_arrive * ss_X.scale_[0] + ss_X.mean_[0]
    return data_pred_departure, data_pred_arrive