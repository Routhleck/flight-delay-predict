import os
import pandas as pd

# 分别读取weather下的所有文件为csv文件
def read_weather_csv():
    # 获取weather文件夹下的所有文件名
    file_list = os.listdir('API/weather')
    # 循环遍历所有文件名
    for file_name in file_list:
        # 读取文件内容
        df = pd.read_csv('API/weather/' + file_name)
        # 去除空行
        df = df.dropna(axis=0, how='any')

        # 去除跟列头相同的行
        df = df.drop_duplicates(subset=['Time'], keep='first')

        # 删除最后一行
        df = df.drop(df.index[-1])

        # 删除所有dp['time'].split('/')[2]!=2016的列
        df = df[df['Time'].str.split('/').str[2] == '2016']
        df['month'] = 0
        df['day'] = 0
        # 创建month 和 day 列
        for i in range(len(df)):
            df['month'].values[i] = df['Time'].values[i].split('/')[1]
            df['day'].values[i] = df['Time'].values[i].split('/')[0]

        # 按month 和 day排序
        df = df.sort_values(by=['month', 'day'])

        # 删除month 和 day 列

        # 写入文件
        df.to_csv('API/weather/' + file_name, index=False)

read_weather_csv()