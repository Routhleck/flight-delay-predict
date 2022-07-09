import joblib
import pandas as pd
from sklearn import preprocessing, metrics, svm
import matplotlib.pyplot as plt

# 预测
def predict(data_train):

    # 删除缺失值NaN
    data_train.dropna(inplace=True)
    # 为出发机场,到达机场,航班编号,年,月,日,时间 字符串转化为可训练的变量
    data_train['出发机场'] = data_train['出发机场'].astype('category')
    data_train['到达机场'] = data_train['到达机场'].astype('category')
    data_train['航班编号'] = data_train['航班编号'].astype('category')
    data_train['时间'] = data_train['时间'].astype('category')

    # 字典映射编码
    data_train['出发机场'] = data_train['出发机场'].cat.codes
    data_train['到达机场'] = data_train['到达机场'].cat.codes
    data_train['航班编号'] = data_train['航班编号'].cat.codes
    data_train['时间'] = data_train['时间'].cat.codes

    cols = ['出发机场','到达机场','航班编号','距离','平均温度','最高温度','最低温度','降水量','气压','风向','风速','年','月','日','时间']
    x = data_train[cols].values

    # 标准化处理
    ss_X = preprocessing.StandardScaler()
    X_train_scaled = ss_X.fit_transform(x)
    # 读取模型
    model = joblib.load('train/delayPredict.pkl')
    # 预测
    delay_cond = model.predict(X_train_scaled)
    # 返回预测结果
    return delay_cond

# 分类模型评估
def evaluate(y_true, y_pred):
    '''print('Accuracy:', metrics.accuracy_score(y_true, y_pred))
    print('Recall:', metrics.recall_score(y_true, y_pred, average='weighted'))
    print('Precision:', metrics.precision_score(y_true, y_pred, average='weighted'))
    print('F1:', metrics.f1_score(y_true, y_pred, average='weighted'))'''

    ACC = metrics.accuracy_score(y_true, y_pred)
    RECALL = metrics.recall_score(y_true, y_pred, average='weighted')
    PREC = metrics.precision_score(y_true, y_pred, average='weighted')
    F1 = metrics.f1_score(y_true, y_pred, average='weighted')
    return ACC, RECALL, PREC, F1
    # 混淆矩阵热力图
    # plt.matshow(metrics.confusion_matrix(y_true, y_pred))
    # plt.show()

# 模型评估
def evaluate_model(y_validation, y_validation_pred):
    ACC, RECALL, PREC, F1 = evaluate(y_validation, y_validation_pred)
    return ACC, RECALL, PREC, F1
