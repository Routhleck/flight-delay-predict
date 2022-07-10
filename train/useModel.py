import pandas as pd
import joblib
from sklearn import preprocessing

# 加载模型
model = joblib.load('train/delayPredict_0710.pkl')
# 加载字典映射csv
id = pd.read_csv('train/dict_id.csv', encoding= 'gbk')
departure = pd.read_csv('train/dict_departure.csv', encoding= 'gbk')
arrival = pd.read_csv('train/dict_arrival.csv', encoding= 'gbk')

# 将id, departure, arrival存储为字典
id_dict = {}
for i in range(len(id)):
    id_dict[id['航班编号'].values[i]] = id['id'].values[i]

departure_dict = {}
for i in range(len(departure)):
    departure_dict[departure['出发机场'].values[i]] = departure['id'].values[i]

arrival_dict = {}
for i in range(len(arrival)):
    arrival_dict[arrival['到达机场'].values[i]] = arrival['id'].values[i]

def predict(data):

    data[0] = departure_dict[data[0]]
    data[1] = arrival_dict[data[1]]
    data[2] = id_dict[data[2]]

    data = pd.DataFrame(data).T

    # 标准化处理
    ss_X = preprocessing.StandardScaler()
    data_scaled = ss_X.fit_transform(data)

    # 预测
    data_pred = model.predict_proba(data_scaled)
    data_pred = data_pred[0]
    # data_pred 取小数点后3位
    data_pred = [round(i, 3) for i in data_pred]
    return data_pred
pred = predict(['HET','TYN','Y87566',165,-6.6,-2.1,-11.1,0.0,1038.0,311.0,10.0,2016,12,5,11])

print('正常延误概率：',pred[0],'% \n轻度延误概率：',pred[1],'% \n中度延误概率：',pred[2],'% \n重度延误概率：',pred[3],'%')