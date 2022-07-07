# 选择起始机场

```python
def setDepartureAirport
# 传入参数：起始机场departureAirport
# 操作：清空selectAirport表，并将机场airport放在selectAirport表中的departureAirport列，然后进行天气预测存到departureWeather表中
```

# 选择到达机场

```python
def setArriveAirport
# 传入参数：到达机场arriveAirport
# 操作：获取selectAirport表中的departureAirport,将arriveAirport放在arriveAirport列，然后进行天气预测存到arriveWeather表中
```

# 延误预测

```python
def delayPredict
# 无参数
# 操作：获取departureWeather表中的天气数据进行预测，更新对应的出发延迟和到达延迟
```

