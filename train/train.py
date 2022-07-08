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

# 导入训练集

data_train = pd.read_csv('dataset/flight_dataset.csv')

# 删除缺失值NaN
data_train.dropna(inplace=True)

cols = ['平均温度', '最高温度', '最低温度', '降水量', '气压', '风向', '风速']
x = data_train[cols].values
y = data_train[['出发延迟']].values


# 划分数据集
X_train, X_validation, y_train, y_validation = train_test_split(x, y, test_size=0.2, random_state=42)

# 标准化处理
ss_X = preprocessing.StandardScaler()
ss_Y = preprocessing.StandardScaler()
X_train_scaled = ss_X.fit_transform(X_train)
y_train_scaled = ss_Y.fit_transform(y_train.reshape(-1, 1))
print(X_train_scaled)
X_validation_scaled = ss_X.transform(X_validation)
y_validation_scaled = ss_Y.transform(y_validation.reshape(-1, 1))


# 建模(注意多标签的问题)

xgb_model = xgb.XGBRegressor(max_depth=3,
                             learning_rate=0.1,
                             n_estimators=100,
                             objective='reg:squarederror',
                             booster='gbtree',
                             random_state=0)

'''
xgb_model = MultiOutputRegressor(xgb.XGBRegressor(max_depth=3,
                             learning_rate=0.1,
                             n_estimators=100,
                             objective='reg:squarederror',
                             booster='gbtree',
                             random_state=0))
'''

# 拟合
xgb_model.fit(X_train_scaled, y_train_scaled)
# 预测
y_validation_pred = xgb_model.predict(X_validation_scaled)
# 反标准化
y_validation_pred = y_validation_pred * ss_Y.scale_[0] + ss_Y.mean_[0]
# data_pred_departure = data_pred_departure * ss_X.scale_[0] + ss_X.mean_[0]
# 保存模型
joblib.dump(xgb_model, 'train/delayPredict.pkl')


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 画图
plt.plot(range(y_validation_scaled.shape[0]), y_validation_scaled, color="blue", linewidth=1.5, linestyle="-")
plt.plot(range(y_validation_pred.shape[0]), y_validation_pred, color="red", linewidth=1.5, linestyle="-.")
plt.legend(['真实值', '预测值'])
plt.title("出发延迟真实值与预测值比对图")
plt.show()  #显示图片


# 模型评估
print('可解释方差值：{}'.format(round(metrics.explained_variance_score(y_validation_scaled, y_validation_pred), 2)))
print('平均绝对误差：{}'.format(round(metrics.mean_absolute_error(y_validation_scaled, y_validation_pred), 2)))
print('均方误差：{}'.format(round(metrics.mean_squared_error(y_validation_scaled, y_validation_pred), 2)))
print('R方值：{}'.format(round(metrics.r2_score(y_validation_scaled, y_validation_pred), 2)))

# 显示重要特征
importances = list(xgb_model.feature_importances_)
data_tmp=data_train.drop(columns=['出发延迟'])
# data_tmp=data_tmp.drop(columns=['到达延迟'])
# data_tmp=data_train.drop(columns=['到达延迟'])
feature_list = list(data_tmp.columns)

feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
feature_importances = sorted(feature_importances, key=lambda x: x[1], reverse=True)

