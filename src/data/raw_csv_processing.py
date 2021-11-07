import numpy as np
import pandas as pd
import json
import time
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import statsmodels.api as sm
from scipy import stats



# 2016

data1 = pd.read_csv('Divvy_Trips_2016_Q1.csv')
data2_4 = pd.read_csv('Divvy_Trips_2016_04.csv')
data2_5 = pd.read_csv('Divvy_Trips_2016_05.csv')
data2_6 = pd.read_csv('Divvy_Trips_2016_06.csv')
data3 = pd.read_csv('Divvy_Trips_2016_Q3.csv')
data4 = pd.read_csv('Divvy_Trips_2016_Q4.csv')

data2016 = pd.concat([data1, data2_4, data2_5, data2_6, data3, data4], ignore_index=True, copy=False)

data2016.rename(columns={'starttime':'start_time', "stoptime": "end_time"}, inplace = True)

repl = lambda s: s.group() + ':00' 
data2016.start_time = data2016.start_time.str.replace(r'\s\d{1,2}:\d\d$', repl)
data2016['time'] = pd.to_datetime(data2016.start_time, format= '%m/%d/%Y %H:%M:%S')

with open('2016_.csv', mode='w', encoding='utf-8') as f_csv:
    data2016.to_csv(f_csv, index=False)



# 2017

data1 = pd.read_csv('Divvy_Trips_2017_Q1.csv')
data2 = pd.read_csv('Divvy_Trips_2017_Q2.csv')
data3 = pd.read_csv('Divvy_Trips_2017_Q3.csv')
data4 = pd.read_csv('Divvy_Trips_2017_Q4.csv')

data2017 = pd.concat([data1, data2, data3, data4], ignore_index=True, copy=False)

repl = lambda s: s.group() + ':00' 
data2017.start_time = data2017.start_time.str.replace(r'\s\d{1,2}:\d\d$', repl)
data2017['time'] = pd.to_datetime(data2017.start_time, format= '%m/%d/%Y %H:%M:%S')

with open('2017.csv', mode='w', encoding='utf-8') as f_csv:
    data2017.to_csv(f_csv, index=False)






# 2018

data1 = pd.read_csv('Divvy_Trips_2018_Q1.csv')
data2 = pd.read_csv('Divvy_Trips_2018_Q2.csv')
data3 = pd.read_csv('Divvy_Trips_2018_Q3.csv')
data4 = pd.read_csv('Divvy_Trips_2018_Q4.csv')

# здесь колонки названы по разному
data1.columns = data2.columns

data2018 = pd.concat([data1, data2, data3, data4], ignore_index=True, copy=False)

# Хранится в текстовом формате с запятыми и точками 
data2018.tripduration = data2018.tripduration.str.slice(stop=-2).str.replace(',', '').astype('int64') 

data2018['time'] = pd.to_datetime(data2018.start_time, format= '%Y/%m/%d %H:%M:%S')

with open('2018.csv', mode='w', encoding='utf-8') as f_csv:
    data2018.to_csv(f_csv, index=False)







# 2019

data1 = pd.read_csv('Divvy_Trips_2019_Q1.csv')
data2 = pd.read_csv('Divvy_Trips_2019_Q2.csv')
data3 = pd.read_csv('Divvy_Trips_2019_Q3.csv')

data2.columns = data1.columns

data2019 = pd.concat([data1, data2, data3], ignore_index=True, copy=False)

data2019.tripduration = data2019.tripduration.str.slice(stop=-2).str.replace(',', '').astype('int64') 

data2019['time'] = pd.to_datetime(data2019.start_time, format= '%Y/%m/%d %H:%M:%S')

with open('2019.csv', mode='w', encoding='utf-8') as f_csv:
    data2019.to_csv(f_csv, index=False)
