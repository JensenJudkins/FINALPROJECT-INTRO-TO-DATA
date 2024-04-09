import pycurl
#parse the json data
import json
import requests
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


#use cfbd to get all players drafted from utah state university
api_key = 'Bearer fvGgHIj0jMLB8BaGzuosEjDXSztCdQnc8JDVoqRANGbSxzYZr+JUoAwrFb5pHzf7'
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
for year in years:
    url = "https://api.collegefootballdata.com/draft/players?year=" + str(year) +"&category=receiving"
    #Save curl response to a file
    c = pycurl.Curl()
    print(year)
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, open('cfbd_draft_data_' + str(year) + '.json', 'wb'))
    c.setopt(c.HTTPHEADER, ['accept: application/json', 'Authorization: ' + api_key])
    c.perform()
    c.close()
    print('finished ' + str(year))

for year in years:
    with open('cfbd_draft_data_' + str(year) + '.json') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        df.to_csv('cfbd_draft_data_' + str(year) + '.csv', index=False)

    


    # response = requests.get(url, headers={"accept": "application", "Authorization": api_key})
    # #Wait for the response

    # data = json.loads(response.text)
    # df = pd.DataFrame(data)
    # df.to_csv('cfbd_draft_data_' + str(year) + '.csv', index=False)

#Combine all the data into one dataframe
df = pd.DataFrame()
for year in years:
    df = df.append(pd.read_csv('cfbd_draft_data_' + str(year) + '.csv'))

#save data to csv
df.to_csv('cfbd_data_raw.csv', index=False)


##Combine data based on playerID
df = pd.read_csv('cfbd_data.csv')
df = df.dropna(subset=['playerId'])
#Combine statType REC to become its own column
df = df.pivot(index='playerId', columns='statType', values='value')
df = df.reset_index()
#Sum REC columns of players with the same playerID
df = df.groupby('playerId').sum()
df = df.reset_index()
df.to_csv('cfbd_data.csv', index=False)




