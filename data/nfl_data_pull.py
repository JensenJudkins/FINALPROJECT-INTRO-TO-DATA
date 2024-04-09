#move receiving data to the correct folder
#Folders where the data will be moved to
#Starting folder /NFL_Stats-main/data/{year}/player/receiving.csv

#Ending folder /nfl_receiving_data/cfbd_recieving_data_{year}.csv

import pandas as pd
import numpy as np
import os

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

for year in years:
    df = pd.read_csv('NFL_Stats-main/data/'+str(year)+'/player/receiving.csv')
    df.to_csv('nfl_receiving_data/cfbd_recieving_data_' + str(year) + '.csv', index=False)
    print('finished ' + str(year))
