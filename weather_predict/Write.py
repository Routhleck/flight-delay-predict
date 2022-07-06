from calendar import isleap
import re
from bs4 import BeautifulSoup
from GetData import GetData
import datetime as DT
import csv


def a(t):
    return t.replace(" - ", "0")


# 功能: 写csv
def write(years, b, c, id):
    """
    :param years: [开始日期距离现在的年份, 结束日期距离现在的年份]
    :param b: [开始日期距离现在日期的天数, 结束日期距离现在日期的天数]
    :param c: csv文件名
    :return: None
    """
    # 1. 创建文件对象
    f = open(c, 'w', encoding='utf-8', newline='')

    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)

    # 3. 构建列表头
    # , "negAve", "negMax", "negMin"
    csv_writer.writerow(["Time", "Ave_t", "Max_t", "Min_t", "Prec", "SLpress", "Winddir", "Windsp"])
    # 取现在日期
    today = DT.datetime.today()
    # 闰年片段
    st = isleap(today.year)
    # 取15天前日期
    week_ago = (today - DT.timedelta(days=b[0])).date()
    # 15天后
    week_pre = (today + DT.timedelta(days=b[1])).date()
    # 从二月到三月
    if week_ago.month + week_pre.month == 5:
        # 开始日期的月份为2月，则为2月到3月
        if week_ago.month == 2 and not st == isleap(today.year - years[0]):  # not后面代表为当不是今年的时候进行下列的处理
            if st:  # 今年为闰年，但是我们要获取的数据的年份并不是，所以进行下列处理
                # 因为今年从2月到三月跨越了2.29，其他年没有，所以我们“向后”多取一天，开始日期减一
                # 今年是，去年或未来不是，所以-1
                week_ago -= DT.timedelta(days=1)
            else:
                # 今年不是，去年或未来是，所以+1
                # 同理，今年不是那就加一，因为其他年有2.29
                week_ago += DT.timedelta(days=1)
    # 爬取数据链接
    # 网站实例
    # http://www.meteomanz.com/sy2?l=1&cou=2250&ind=54511
    # &d1=08
    # &m1=06
    # &y1=2022
    # &d2=21
    # &m2=06
    # &y2=2022
    url = "http://www.meteomanz.com/sy2?l=1&cou=2250&ind=" + id + "&d1=" + str(week_ago.day).zfill(2) + "&m1=" + str(
        week_ago.month).zfill(2) + "&y1=" + str(week_ago.year - years[0]) + "&d2=" + str(week_pre.day).zfill(
        2) + "&m2=" + str(week_pre.month).zfill(2) + "&y2=" + str(week_pre.year - years[1])
    # 显示获取数据集的网址
    print(url)
    g = GetData(url).Get()
    # beautifulsoup解析网页
    soup = BeautifulSoup(g, "html5lib")
    # 取<tbody>内容
    tb = soup.find(name="tbody")
    # 取tr内容
    past_tr = tb.find_all(name="tr")
    for tr in past_tr:
        # 取tr内每个td的内容
        text = tr.find_all(name="td")
        flag = False
        negA = negMax = negMin = False
        for i in range(0, len(text)):
            if i == 0:
                text[i] = text[i].a.string
                # 网站可能bug，会给每个月第0天，比如 00/6/2022,所以要drop掉
                if "00/" in text[i]:
                    flag = True
            elif i == 8:
                # 把/8去掉，网页显示的格式
                text[i] = text[i].string.replace("/8", "")
                print('第八')
                print(text[8])
            elif i == 5:
                # 去掉单位
                text[i] = text[i].string.replace(" Hpa", "")
                print('第五')
                print(text[5])
            elif i == 6:
                # 去掉风力里括号内的内容
                text[i] = re.sub(u"[º(.*?|N|W|E|S)]", "", text[i].string)
                print('第六')
                print(text[6])
            else:
                # 取每个元素的内容
                text[i] = text[i].string
                print('分割线：text')
                print(text)
            # 丢失数据都取空值
            text[i] = "" if text[i] == "-" else text[i]
            text[i] = "" if text[i] == "- " else text[i]
            text[i] = "" if text[i] == "Tr" else text[i]
        print(len(text))
        text = text[0:8]
        # 4. 写入csv文件内容
        if not flag:
            csv_writer.writerow(text)
    # 5. 关闭文件
    f.close()
