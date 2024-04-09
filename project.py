# %%
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# %%
#load json file
df = pd.read_json('games_1512362753.8735218.json')
df.head()


# %%
import cfbd

#use cfbd to get all players drafted from utah state university
api_key = 'Bearer fvGgHIj0jMLB8BaGzuosEjDXSztCdQnc8JDVoqRANGbSxzYZr+JUoAwrFb5pHzf7'

cfbd_client = cfbd.ApiClient(api_key)

#search for all players drafted from utah state university
utah_state_draft_picks = cfbd_client.draft_picks.search(team='Utah State')

#convert to dataframe
utah_state_draft_picks_df = pd.DataFrame(utah_state_draft_picks)
utah_state_draft_picks_df.head()



