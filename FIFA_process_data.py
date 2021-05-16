import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import statsmodels.api as sm
import xgboost as xgb
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler

df = pd.read_csv('/FIFA/results.csv')

Desc = df.describe()
# print(df.describe())
# print(df.info())
# print(df.columns)

# # Null = df.isnull().sum()
# plt.figure(figsize = (12,6))
# ax = sns.heatmap(df.isnull(),cmap ='gray')
# Duplicates = df[df.duplicated()]


# # # JUNK
# #Column for Ground (Home,Away,Neutral) 
# #Ireland, Bohemia will be exception
# for i in df.index:
#     if (df['country'][i]=='Republic of Ireland' or df['country'][i]=='Northern Ireland' or df['country'][i]=='Irish Free State'):
#         df['country'][i] = 'Northern Ireland'
#         df['home_team'][i] = 'Northern Ireland'
#         df['away_team'][i] = 'Northern Ireland'
#     if (df['country'][i]=='Czechoslovakia' or df['country'][i]=='Bohemia' or df['country'][i]=='Czech Republic'):
#         df['country'][i] = 'Czechoslovakia' 
#         df['home_team'][i] = 'Czechoslovakia'
#         df['away_team'][i] = 'Czechoslovakia'
#     if (df['country'][i]=='Catalonia' or df['country'][i]=='Spain'):
#         df['country'][i] = 'Spain' 
#         df['home_team'][i] = 'Spain'
#         df['away_team'][i] = 'Spain'
#     if (df['country'][i]=='Brittany' or df['country'][i]=='France'):
#         df['country'][i] = 'France' 
#         df['home_team'][i] = 'France'
#         df['away_team'][i] = 'France'
#     if (df['country'][i]=='British Guyana' or df['country'][i]=='Guyana' or df['country'][i]=='Barbados'):
#         df['country'][i] = 'Barbados' 
#         df['home_team'][i] = 'Barbados'
#         df['away_team'][i] = 'Barbados'
#     if (df['country'][i]=='Soviet Union' or df['country'][i]=='Russia'):
#         df['country'][i] = 'Russia' 
#         df['home_team'][i] = 'Russia'
#         df['away_team'][i] = 'Russia'
#     if (df['country'][i]=='Netherlands Guyana' or df['country'][i]=='Suriname'):
#         df['country'][i] = 'Suriname' 
#         df['home_team'][i] = 'Suriname'
#         df['away_team'][i] = 'Suriname'
# #Just to check
# df['Won_by_team'] = df['away_team'] 
# for i in df.index:
#     if df['home_team'][i] == df['country'][i]:
#         df['Won_by_team'][i] = 'H'
#     elif df['away_team'][i] == df['country'][i]:
#         df['Won_by_team'][i] = 'A'
#     else :
#         df['Won_by_team'][i] = 'N'


#Adding a column for winner team
df['Winner'] = df['away_team'] 
for i in df.index:
    if df['home_score'][i] > df['away_score'][i]:
        df['Winner'][i] = df['home_team'][i]
    elif df['home_score'][i] == df['away_score'][i]:
        df['Winner'][i] = 'Tie'


#Adding a column for by how much goals team won
df['Won_by_goals'] = df['away_team'] 
df['Won_by_goals'] = abs(df['home_score'] - df['away_score'])


#From dates getting years and months
df['Year'] = pd.DatetimeIndex(df['date']).year
df['Month'] = pd.DatetimeIndex(df['date']).month_name()
df.drop(['date'], axis = 1, inplace = True)

#Adding column for total goals ana matches for count
df['Total_goals'] = df['home_score']+df['away_score']
df['matches'] = 1
df['Tie'] = np.where(df['Winner'] == 'Tie',1,0)

#Let us add column for Winner:H/A/T
df['H/A/T'] = np.where(df['Winner'] !='Tie',np.where(df['Winner']==df['home_team'],'H','A'),'T')



df.to_csv('/FIFA/processed_data.csv',index =False)

