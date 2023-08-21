![img](https://img.shields.io/apm/l/vim-mode)       ![img](https://img.shields.io/github/contributors/Routhleck/flight-delay-predict)     ![img](https://img.shields.io/github/stars/Routhleck/flight-delay-predict?style=social)    ![img](https://img.shields.io/github/forks/Routhleck/flight-delay-predict?style=social)  ![img](https://img.shields.io/github/watchers/Routhleck/flight-delay-predict?style=social) 
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

# flight-delay-predict
[English](README.md)|[中文](README_CN.md)

flight delay predict with weather data

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片1.png)

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片2.png)

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片3.png)

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片4.png)

# 注意⚠⚠⚠

## 数据库

数据库初始化文件在`dataset-and-model`的branch中，design文件夹下的all.sql，

**注意！！，因为在答辩时天气预测时的爬虫网站出错，所以临时换用了其他的方法，需要在`arriveweather`这个表里加上`departureweather`的`year, month, day, normal_prob, mild_prob, moderate_prob, serious_prob`的相同属性，并删除`date`属性**

其次还需要INSERT`airline`和`airport`这两个表的数据，分别在`delay-master`branch的`modelTrain/predict/dict_id.csv`和`dataset-and-model`branch的`dataset/airport.csv`

最后别忘了在`API/algorithm.py`和`API/loginAndRegister.py`开始重新配置你的(云)数据库

## 天气数据预测

因为答辩的时候，爬取的天气网站临时维护，所以被迫将气象预测换成直接读取往年同一天的消息，现在已经能重新使用，如果需要加入天气预测则可以再algorithm.py(如果我没记错的话)重新恢复下天气预测功能

<!-- ALL-CONTRIBUTORS-LIST: START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
# 项目
基于往年航班和天气信息的对航班延迟信息的预测系统

数据清洗项目

1. 首先根据原航班信息数据对应天气信息网站手动做出机场-城市编码参考字典，其中只选择了部分机场

2. 对应填充机场的经纬度

3. 首先进行第一次清洗：删除出发、到达机场不在给出的参考机场字典中的项

4. 进行第二次清洗：删除同一时间航线（即为出发地点和到达地点都一样的航班）重复的项

5. 其中对最原始的数据集的处理还有：

  通过原始的时间戳计算计划出发、达到与实际出发、达到的时间

  通过不同机场之间的经纬度计算出各个机场之间的距离并整合填充至各个航班相应的信息栏中

6. 通过构建的机场-城市参考字典进行天气信息的爬取、填充

  首先构建不同城市的各个的以天为单位的天气信息文件.CSV

  进行相应的网络爬虫读取数据并写道城市天气文件中

  通过城市->定位所要访问的文件；预计出发日期->定位到具体要填充的项

7. 之后保存写入，得到初始清洗好的数据集了


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

#Project Dependence
npm install echarts@4.9
npm install --save-dev less-loader less


### 人员分工：

  #### 项目经理 解世超

  #### 前端工程师 蒋涵、陈泽锋

  #### 后端工程师 何毅、江顺

  #### 数据工程师 贺思超

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Routhleck"><img src="https://avatars.githubusercontent.com/u/88108241?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Routhleck Ekalesor</b></sub></a><br /><a href="#data-Routhleck" title="Data">🔣</a> <a href="https://github.com/Routhleck/flight-delay-predict/commits?author=Routhleck" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/heyi755"><img src="https://avatars.githubusercontent.com/u/85550446?v=4?s=100" width="100px;" alt=""/><br /><sub><b>是小柴同学吖</b></sub></a><br /><a href="https://github.com/Routhleck/flight-delay-predict/commits?author=heyi755" title="Code">💻</a> <a href="https://github.com/Routhleck/flight-delay-predict/issues?q=author%3Aheyi755" title="Bug reports">🐛</a> <a href="#infra-heyi755" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/Shigakki"><img src="https://avatars.githubusercontent.com/u/92007182?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shichao</b></sub></a><br /><a href="https://github.com/Routhleck/flight-delay-predict/commits?author=Shigakki" title="Documentation">📖</a> <a href="#ideas-Shigakki" title="Ideas, Planning, & Feedback">🤔</a> <a href="#projectManagement-Shigakki" title="Project Management">📆</a></td>
    <td align="center"><a href="https://github.com/chenzefeng33"><img src="https://avatars.githubusercontent.com/u/87693985?v=4?s=100" width="100px;" alt=""/><br /><sub><b>chenzefeng33</b></sub></a><br /><a href="#design-chenzefeng33" title="Design">🎨</a> <a href="#platform-chenzefeng33" title="Packaging/porting to new platform">📦</a></td>
    <td align="center"><a href="https://github.com/hanjiang1073"><img src="https://avatars.githubusercontent.com/u/95728193?v=4?s=100" width="100px;" alt=""/><br /><sub><b>hanjiang1073</b></sub></a><br /><a href="#design-hanjiang1073" title="Design">🎨</a> <a href="#platform-hanjiang1073" title="Packaging/porting to new platform">📦</a></td>
    <td align="center"><a href="https://github.com/1avish"><img src="https://avatars.githubusercontent.com/u/103949635?v=4?s=100" width="100px;" alt=""/><br /><sub><b>1avish</b></sub></a><br /><a href="https://github.com/Routhleck/flight-delay-predict/commits?author=1avish" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
