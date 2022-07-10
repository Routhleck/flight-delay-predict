import pandas as pd


def generate_dict_csv():
    data_train = pd.read_csv('dataset/flight_final.csv', encoding= 'utf-8')
    print('读取完成')

    # 删除缺失值
    data_train.dropna(inplace=True)
    # 为出发机场,到达机场,航班编号 字符串转化为可训练的变量
    data_train['出发机场'] = data_train['出发机场'].astype('category')
    data_train['到达机场'] = data_train['到达机场'].astype('category')
    data_train['航班编号'] = data_train['航班编号'].astype('category')

    # 字典映射编码
    data_train['出发机场'] = data_train['出发机场'].cat.codes
    data_train['到达机场'] = data_train['到达机场'].cat.codes
    data_train['航班编号'] = data_train['航班编号'].cat.codes

    # 字典存储
    data_train.to_csv('dataset/flight_final_encoded.csv', index=False)

def generate_dict():
    # 分别读取flight_final.csv和flight_final_encoded.csv
    data_train = pd.read_csv('dataset/flight_final.csv', encoding= 'utf-8')
    data_train_encoded = pd.read_csv('dataset/flight_final_encoded.csv', encoding= 'utf-8')

    # 删除缺失值
    data_train.dropna(inplace=True)
    data_train_encoded.dropna(inplace=True)

    # 将data_train中的出发机场,到达机场,航班编号与data_train_encoded中的出发机场,到达机场,航班编号一一对应，生成字典
    dict_id = {}
    for i in range(len(data_train)):
        dict_id[data_train['航班编号'].values[i]] = data_train_encoded['航班编号'].values[i]
    # 将dict_id存储为字典文件
    with open('dataset/dict_id.txt', 'w') as f:
        for key in dict_id:
            f.write(key + ',' + str(dict_id[key]) + '\n')
    dict_departure = {}
    for i in range(len(data_train)):
        dict_departure[data_train['出发机场'].values[i]] = data_train_encoded['出发机场'].values[i]
    with open('dataset/dict_departure.txt', 'w') as f:
        for key in dict_departure:
            f.write(key + ',' + str(dict_departure[key]) + '\n')
    
    dict_arrival = {}
    for i in range(len(data_train)):
        dict_arrival[data_train['到达机场'].values[i]] = data_train_encoded['到达机场'].values[i]
    with open('dataset/dict_arrival.txt', 'w') as f:
        for key in dict_arrival:
            f.write(key + ',' + str(dict_arrival[key]) + '\n')

generate_dict()