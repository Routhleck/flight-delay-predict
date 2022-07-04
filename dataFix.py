import pandas as pd

# 读取dataset/flight_reduced_unique.csv文件
# 删除不需要的列
origin_dataset = pd.read_csv('dataset/flight_reduced_unique.csv')
print('成功读取flight_reduced_unique.csv文件')
origin_dataset = origin_dataset.drop(['DAY_OF_WEEK', 'AIRLINE', 'FLIGHT_NUMBER', 'TAIL_NUMBER', 
                                    'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME', 'TAXI_OUT', 
                                    'WHEELS_OFF', 'SCHEDULED_TIME', 'ELAPSED_TIME', 
                                    'AIR_TIME', 'WHEELS_ON', 'TAXI_IN', 'SCHEDULED_ARRIVAL', 
                                    'ARRIVAL_TIME', 'DIVERTED', 'CANCELLED', 'CANCELLATION_REASON', 
                                    'AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 
                                    'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY'], axis=1)
print('成功删除不需要的列')
# 保存缩减后的数据集
origin_dataset.to_csv('dataset/flight_fix.csv', index=False)