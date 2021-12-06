import numpy as np
import pandas as pd
import json
import time
import matplotlib.pyplot as plt
import datetime

def process_raw_csv(path1, path2, out_path):

    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)

    data2.columns = data1.columns

    data2019 = pd.concat([data1, data2], ignore_index=True, copy=False)

    data2019.tripduration = data2019.tripduration.str.slice(stop=-2).str.replace(',', '').astype('int64') 

    data2019['time'] = pd.to_datetime(data2019.start_time, format= '%Y/%m/%d %H:%M:%S')

    with open(out_path, mode='w', encoding='utf-8') as f_csv:
        data2019.to_csv(f_csv, index=False)