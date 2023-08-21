![img](https://img.shields.io/apm/l/vim-mode)       ![img](https://img.shields.io/github/contributors/Routhleck/flight-delay-predict)     ![img](https://img.shields.io/github/stars/Routhleck/flight-delay-predict?style=social)    ![img](https://img.shields.io/github/forks/Routhleck/flight-delay-predict?style=social)  ![img](https://img.shields.io/github/watchers/Routhleck/flight-delay-predict?style=social) 
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

# flight-delay-predict
[English](README.md)|[中文](README_CN.md)

Predicting flight delays with weather data.

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片1.png)

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片2.png)

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片3.png)

![img](https://raw.githubusercontent.com/Routhleck/flight-delay-predict/delay-master/img/图片4.png)

# Caution ⚠⚠⚠

## Database

Database initialization files are located in the `dataset-and-model` branch, under the design folder in all.sql.

**Note!! Due to an error with the weather prediction website during the presentation, another method was temporarily used. You'll need to add the same attributes from `departureweather` (`year, month, day, normal_prob, mild_prob, moderate_prob, serious_prob`) to the `arriveweather` table and delete the `date` attribute.**

Next, you need to INSERT data into the `airline` and `airport` tables, which are located in the `delay-master` branch's `modelTrain/predict/dict_id.csv` and the `dataset-and-model` branch's `dataset/airport.csv`, respectively.

Finally, don't forget to reconfigure your (cloud) database in `API/algorithm.py` and `API/loginAndRegister.py`.

## Weather Data Prediction

During the defense, the weather site being scraped was temporarily down, so weather predictions were replaced with data from the same day in previous years. It can now be used again. If you need to reintegrate weather predictions, you can restore the weather prediction function in algorithm.py (if I recall correctly).

<!-- ALL-CONTRIBUTORS-LIST: START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
# Project
A flight delay prediction system based on previous years' flight and weather information.

Data Cleaning Project:

1. First, manually create an airport-city code reference dictionary based on the original flight information data. Only a selection of airports is chosen.
2. Fill in the corresponding airport longitude and latitude.
3. First, clean: remove items where the departure and arrival airports are not in the provided reference airport dictionary.
4. Second cleaning: remove duplicated items for the same flight route (i.e., where departure and arrival points are the same).
5. The handling of the most original dataset also includes:
  - Calculate the planned departure, arrival, actual departure, and arrival times from the original timestamp.
  - Calculate the distance between different airports based on their longitude and latitude and integrate it into the corresponding flight information column.
6. Scrape and fill in weather information using the constructed airport-city reference dictionary.
  - First, construct daily weather information files for different cities in .CSV format.
  - Scrape data through web crawlers and write to the city weather file.
  - Use the city to locate the file to access; the estimated departure date to locate the specific item to fill.
7. Finally, save the input to get the initially cleaned dataset.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

# Project Dependence
npm install echarts@4.9
npm install --save-dev less-loader less

### Team Allocation:

  #### Project Manager: 解世超 (Jie Shichao)
  
  #### Front-end Engineers: 蒋涵 (Jiang Han), 陈泽锋 (Chen Zefeng)
  
  #### Back-end Engineers: 何毅 (He Yi), 江顺 (Jiang Shun)
  
  #### Data Engineers: 贺思超 (He Sichao)

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

