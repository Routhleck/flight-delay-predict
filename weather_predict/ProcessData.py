from Write import write
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt


# 数据预处理
def ProcessData(city, id):
    """
    :return:
        [X_train X训练数据集,
        X_valid X训练数据集的验证集,
        y_train Y训练数据集,
        y_valid Y训练数据集的验证集,
        imputed_X_test 预测数据集]
    """

    # 用近几年的数据做训练集
    # 如 [1,1], [20, 0]就是用2021年的今天的20天前到2021年的今天数据做训练集
    # 写入csv
    
    id = str(id)
    write([1, 1], [15, 0], "weather_predict/weather_train_train.csv", id)
    write([1, 1], [0, 15], "weather_predict/weather_train_valid.csv", id)
    write([0, 0], [15, 0], "weather_predict/weather_test.csv", id)
    X_test = pd.read_csv("weather_predict/weather_test.csv", index_col="Time", parse_dates=True)
    # 读取测试集和验证集
    X = pd.read_csv("weather_predict/weather_train_train.csv", index_col="Time", parse_dates=True)
    y = pd.read_csv("weather_predict/weather_train_valid.csv", index_col="Time", parse_dates=True)
    
    # 填充缺少的数值
    my_imputer = SimpleImputer()
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
    imputed_y_train = pd.DataFrame(my_imputer.fit_transform(y_train))
    imputed_y_valid = pd.DataFrame(my_imputer.transform(y_valid))
    imputed_X_test = pd.DataFrame(my_imputer.fit_transform(X_test))

    return [imputed_X_train, imputed_X_valid, imputed_y_train, imputed_y_valid, imputed_X_test]
