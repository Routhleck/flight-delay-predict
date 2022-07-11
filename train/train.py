import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import norm
from sklearn import preprocessing, metrics, svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.multioutput import MultiOutputRegressor
import joblib
import xgboost as xgb
from predict_test import evaluate_model

def train_test(max_depth, learning_rate, objective, booster, n_jobs, min_child_weight, gamma, subsample, colsample_bytree):
    # 导入训练集

    data_train = pd.read_csv('../dataset/flight_final.csv', encoding= 'utf-8')
    print('读取完成')

    # 删除缺失值NaN
    data_train.dropna(inplace=True)
    # 为出发机场,到达机场,航班编号,年,月,日,时间 字符串转化为可训练的变量
    data_train['出发机场'] = data_train['出发机场'].astype('category')
    data_train['到达机场'] = data_train['到达机场'].astype('category')
    data_train['航班编号'] = data_train['航班编号'].astype('category')

    # 字典映射编码
    data_train['出发机场'] = data_train['出发机场'].cat.codes
    data_train['到达机场'] = data_train['到达机场'].cat.codes
    data_train['航班编号'] = data_train['航班编号'].cat.codes

    cols = ['出发机场','到达机场','航班编号','距离','平均温度','最高温度','最低温度','降水量','气压','风向','风速','年','月','日','时间']
    x = data_train[cols].values
    y = data_train[['延迟程度']].values

    # 取5%作为训练验证集


    # 划分数据集
    X_train, X_validation, y_train, y_validation = train_test_split(x, y, test_size=0.02, random_state=42)
    print('划分完成')

    # 标准化处理
    ss_X = preprocessing.StandardScaler()
    X_train_scaled = ss_X.fit_transform(X_train)
    # print(X_train_scaled)
    X_validation_scaled = ss_X.transform(X_validation)


    # 建模(注意多标签的问题)
    print('开始建模')

    xgb_model = xgb.XGBClassifier(max_depth=max_depth,
                                learning_rate= learning_rate,
                                n_estimators=200,
                                objective= objective,
                                booster= booster,
                                n_jobs= n_jobs,
                                min_child_weight= min_child_weight,
                                gamma= gamma,
                                subsample= subsample,
                                colsample_bytree= colsample_bytree
                                )

    # 使用cv函数确定n_estimators的数量
    '''xgb_param = xgb_model.get_xgb_params()
    xgtrain = xgb.DMatrix(X_train_scaled, label=y_train)
    cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=xgb_model.get_params()['n_estimators'], nfold=5, metrics='auc', early_stopping_rounds=50)
    xgb_model.set_params(n_estimators=cvresult.shape[0])
    '''

    print(xgb_model.get_params())

    '''
    xgb_model = MultiOutputRegressor(xgb.XGBRegressor(max_depth=3,
                                learning_rate=0.1,
                                n_estimators=100,
                                objective='reg:squarederror',
                                booster='gbtree',
                                random_state=0))
    '''

    # 拟合
    xgb_model.fit(X_train_scaled, y_train)
    print('拟合完成')
    # 预测
    y_validation_pred = xgb_model.predict(X_validation_scaled)

    # data_pred_departure = data_pred_departure * ss_X.scale_[0] + ss_X.mean_[0]

    # 保存模型
    joblib.dump(xgb_model, '../train/delayPredict_test.pkl')

    # 评估模型
    ACC, RECALL, PREC, F1 = evaluate_model(y_validation, y_validation_pred)
    return ACC, RECALL, PREC, F1
'''
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 画图
plt.plot(range(y_validation.shape[0]), y_validation, color="blue", linewidth=1.5, linestyle="-")
plt.plot(range(y_validation_pred.shape[0]), y_validation_pred, color="red", linewidth=1.5, linestyle="-.")
plt.legend(['真实值', '预测值'])
plt.title("出发延迟真实值与预测值比对图")
plt.show()  #显示图片


# 分类模型

# 显示重要特征
importances = list(xgb_model.feature_importances_)
data_tmp=data_train.drop(columns=['延迟程度'])
# data_tmp=data_tmp.drop(columns=['到达延迟'])
# data_tmp=data_train.drop(columns=['到达延迟'])
feature_list = list(data_tmp.columns)

feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
feature_importances = sorted(feature_importances, key=lambda x: x[1], reverse=True)
'''

