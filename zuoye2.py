# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:41:05 2018
联网
导入json包
@author: lenovo
"""

import urllib.request as r
city=input("请输入城市拼音:")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 '
info=r.urlopen(url.format(city)).read().decode('utf-8','ignore')
import json
#第一天
data=json.loads(info)
a=data['list'][4]['dt_txt']#提取当前城市的具体日期
b=data['list'][4]['main']['temp']#温度
d=data['list'][4]['main']['temp_max']#最高温度
e=data['list'][4]['weather'][0]['description']#天气情况
c=data['list'][4]['main']['pressure']#气压
print("{}".format(a)+"\n"+
      "该城市的温度是:{}摄氏度".format(b)+"\n"+
      "最高可达到:{}摄氏度".format(d)+"\n"+
      "气压为:{}".format(c)+"\n"+
      "{}天".format(e))
#第二天
a=data['list'][12]['dt_txt']#提取当前城市的具体日期
b=data['list'][12]['main']['temp']#温度
d=data['list'][12]['main']['temp_max']#最高温度
e=data['list'][12]['weather'][0]['description']#天气情况
c=data['list'][12]['main']['pressure']#气压
print("{}".format(a)+"\n"+
      "该城市的温度是:{}摄氏度".format(b)+"\n"+
      "最高可达到:{}摄氏度".format(d)+"\n"+
      "气压为:{}".format(c)+"\n"+
      "{}天".format(e))
#第三天
a=data['list'][20]['dt_txt']#提取当前城市的具体日期
b=data['list'][20]['main']['temp']#温度
d=data['list'][20]['main']['temp_max']#最高温度
e=data['list'][20]['weather'][0]['description']#天气情况
c=data['list'][20]['main']['pressure']#气压
print("{}".format(a)+"\n"+
      "该城市的温度是:{}摄氏度".format(b)+"\n"+
      "最高可达到:{}摄氏度".format(d)+"\n"+
      "气压为:{}".format(c)+"\n"+
      "{}天".format(e))
#第四天
a=data['list'][28]['dt_txt']#提取当前城市的具体日期
b=data['list'][28]['main']['temp']#温度
d=data['list'][28]['main']['temp_max']#最高温度
e=data['list'][28]['weather'][0]['description']#天气情况
c=data['list'][28]['main']['pressure']#气压
print("{}".format(a)+"\n"+
     "该城市的温度是:{}摄氏度".format(b)+"\n"+
      "最高可达到:{}摄氏度".format(d)+"\n"+
      "气压为:{}".format(c)+"\n"+
      "{}天".format(e))
#第五天
a=data['list'][36]['dt_txt']#提取当前城市的具体日期
b=data['list'][36]['main']['temp']#温度
d=data['list'][36]['main']['temp_max']#最高温度
e=data['list'][36]['weather'][0]['description']#天气情况
c=data['list'][36]['main']['pressure']#气压
print("{}".format(a)+"\n"+
     "该城市的温度是:{}摄氏度".format(b)+"\n"+
      "最高可达到:{}摄氏度".format(d)+"\n"+
      "气压为:{}".format(c)+"\n"+
      "{}天".format(e))