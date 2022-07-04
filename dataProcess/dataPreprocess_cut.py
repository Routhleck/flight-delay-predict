import pandas as pd
#缩减数据集

# 读取dataset/flight.csv文件
origin_dataset = pd.read_csv('dataset/flights.csv')
print('成功读取flights.csv文件')
# 删除ORIGIN_AIRPORT行中没有dataset/airports.csv中的IATA_CODE的行
airport = pd.read_csv('dataset/airports.csv')
print('成功读取airports.csv文件')
select_airport = airport['IATA_CODE'].values

# 将origin_dataset中的ORIGIN_AIRPORT列中的值与select_airport中的值进行比较，如果不在select_airport中，则删除该行
origin_dataset = origin_dataset[origin_dataset['ORIGIN_AIRPORT'].isin(select_airport)]
print('成功删除ORIGIN_AIRPORT不在airports.csv中的行')
# 保存缩减后的数据集
origin_dataset.to_csv('dataset/flight_reduced.csv', index=False)

# 相同的ORIGIN_AIRPORT 仅保留相同YEAR,MONTH,DAY,DAY_OF_WEEK的一行
origin_dataset = origin_dataset.drop_duplicates(subset=['ORIGIN_AIRPORT', 'YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK'])
print('成功删除相同ORIGIN_AIRPORT的行')
# 保存缩减后的数据集
origin_dataset.to_csv('dataset/flight_reduced_unique.csv', index=False)