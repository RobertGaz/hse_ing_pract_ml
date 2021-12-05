import numpy as np
import pandas as pd
import json
import time
import matplotlib.pyplot as plt
import datetime



# 2019

data1 = pd.read_csv('../../data/raw/Divvy_Trips_2019_Q1.csv')
data2 = pd.read_csv('../../data/raw/Divvy_Trips_2019_Q2.csv')

data2.columns = data1.columns

data2019 = pd.concat([data1, data2], ignore_index=True, copy=False)

data2019.tripduration = data2019.tripduration.str.slice(stop=-2).str.replace(',', '').astype('int64') 

data2019['time'] = pd.to_datetime(data2019.start_time, format= '%Y/%m/%d %H:%M:%S')

with open('../../data/processed/2019.csv', mode='w', encoding='utf-8') as f_csv:
    data2019.to_csv(f_csv, index=False)