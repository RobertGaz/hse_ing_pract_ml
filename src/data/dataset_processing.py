import numpy as np
import pandas as pd
import json
import time
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import statsmodels.api as sm
from scipy import stats

data2016 = pd.read_csv('2016_.csv')
data2017 = pd.read_csv('2017_.csv')
data2018 = pd.read_csv('2018_.csv')
data2019 = pd.read_csv('2019_.csv')

df = pd.concat([data2016, data2017, data2018, data2019], ignore_index=True, copy=False)
df.drop_duplicates(subset='trip_id', inplace=True)
df.drop(columns = ['usertype', 'start_time', 'end_time', 'trip_id', 'bikeid', 'from_station_id', 'from_station_name', 'to_station_id', 'to_station_name'], inplace=True)
df.dropna(subset=['gender', 'birthyear'], inplace=True)

df.gender = df.gender.astype('category')
df.birthyear = df.birthyear.astype('int')
df.index = pd.to_datetime(df.time, format='%Y/%m/%d %H:%M:%S')
df.drop(columns=['time'], inplace = True)
df['year'] = df.index.year.values
df['month'] = df.index.month.values
df['hour'] = df.index.hour.values
df['week_day'] = df.index.weekday.values + 1

df['age'] = df.year - df.birthyear

df.drop(columns=['birthyear'], inplace=True)

# Будем измерять длительность поездки в минутах
df.tripduration /=60


# В датасете имеются аномалии в виде аренд длительностью в тысячи минут:
df.sort_values('tripduration', ascending=False).head(5)

# Возможно, это случаи с забытыми велосипедами или несработавшими датчиками при закреплении велосипеда на станции и т.д.
# Так или иначе, такие аренды считать поездками мы не будем


# 99 процентов всех поездок длились меньше ~57 минут:


np.percentile(df.tripduration, 99)

# Для удобства работы с данными ограничимся арендой 60 минут. Этого более, чем достаточно
df = df[df.tripduration < 60]


# Save assembled data to file:

with open('ALL.csv', mode='w', encoding='utf-8') as f_csv:
    df.to_csv(f_csv)

# Read assembled data from file:

df = pd.read_csv('ALL.csv')

df.index = pd.to_datetime(df.time, format='%Y/%m/%d %H:%M:%S')

df.drop(columns='time', inplace=True)

df.sort_index(inplace=True)
