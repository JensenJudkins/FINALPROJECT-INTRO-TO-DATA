
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import json
import requests
import time
import os


api_key = 'Bearer fvGgHIj0jMLB8BaGzuosEjDXSztCdQnc8JDVoqRANGbSxzYZr+JUoAwrFb5pHzf7'
#'Colorado State','BYU', 'Clemson','Georgia','Harvard','Hawaii','Idaho State','James Madison','LSU','Michigan','Oaklahoma','Ohio State','Oregon', 'Penn State', 'South Dakota', 'Texas', 'UCLA', 'Washington', 'Utah State', 'Wyoming', 'Air Force', 'Boise State'
large_schools = ['Alabama', 'Auburn', 'Florida', 'Georgia', 'LSU', 'Michigan', 'Notre Dame', 'Ohio State', 'Oklahoma', 'Oregon', 'Penn State', 'Texas', 'USC', 'Wisconsin']
medium_schools = ['Arizona', 'Arizona State', 'Arkansas', 'Boston College', 'BYU', 'California', 'Clemson', 'Colorado', 'Florida State', 'Georgia Tech', 'Iowa', 'Iowa State', 'Kansas', 'Kansas State', 'Kentucky', 'Louisville', 'Maryland', 'Miami', 'Michigan State', 'Minnesota', 'Mississippi State', 'Missouri', 'Nebraska', 'North Carolina', 'North Carolina State', 'Northwestern', 'Oklahoma State', 'Oregon State', 'Pittsburgh', 'Purdue', 'Rutgers', 'South Carolina', 'Stanford', 'Syracuse', 'TCU', 'Tennessee', 'Texas A&M', 'Texas Tech', 'UCLA', 'Utah', 'Virginia', 'Virginia Tech', 'Washington', 'Washington State', 'West Virginia']
small_schools = ['Air Force', 'Akron', 'Appalachian State', 'Arkansas State', 'Army', 'Ball State', 'Boise State', 'Bowling Green', 'Buffalo', 'Central Michigan', 'Charlotte', 'Cincinnati', 'Coastal Carolina', 'Colorado State', 'Connecticut', 'Duke', 'Eastern Michigan', 'East Carolina', 'Florida Atlantic', 'Florida International', 'Fresno State', 'Georgia Southern', 'Georgia State', 'Hawaii', 'Houston', 'Illinois', 'Indiana', 'Kent State', 'Liberty', 'Louisiana', 'Louisiana Tech', 'Louisiana-Monroe', 'Marshall', 'Memphis', 'Miami (OH)', 'Middle Tennessee', 'Navy', 'Nevada', 'New Mexico', 'New Mexico State', 'North Texas', 'Northern Illinois', 'Ohio', 'Old Dominion', 'Rice', 'San Diego State', 'San Jose State', 'SMU', 'South Alabama', 'South Florida', 'Southern Miss', 'Temple', 'Texas State', 'Toledo', 'Troy', 'Tulane', 'Tulsa', 'UAB', 'UCF', 'UNLV', 'UTEP', 'UTSA', 'UTah State', 'UTah State', 'Western Kentucky', 'Western Michigan', 'Wyoming']

all_schools = large_schools + medium_schools + small_schools


teams = all_schools
headers = {
    "accept": "application/json",
    "Authorization": api_key
}

for team in teams:
    try:
        os.mkdir('draft_data/'+team)
    except:
        pass


#use cfbd to get all recieving stats for utah state university from 2011 to 2022
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
for team in teams:
    for year in years:
        url = "https://api.collegefootballdata.com/draft/picks"
        parameters = {
            "year": year,
            "college": team
        }
        response = requests.get(url, headers=headers, params=parameters)
        x = pd.DataFrame(json.loads(response.text))
        print(x)
        x.to_csv('draft_data/'+team + '/cfbd_draft_data_' + str(year) + '.csv', index=False)




