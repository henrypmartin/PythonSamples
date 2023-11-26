'''
Created on 24-Nov-2023

@author: Nomura
'''
import pandas as pd
from pandas.core.series import Series as series
from pandas.core.groupby.generic import SeriesGroupBy as seriesGB
import random

df = pd.read_csv("C:\\Henry\\Learning\\IISC_CDC\\Python\\goals.txt", 
                 delimiter=";", header=None, usecols=[0,1,2])

df.columns = ['Player', 'Country', 'Time']

print("\n\n")
maxGoalsCntry = df['Country'].value_counts().idxmax()
maxGoals = df['Country'].value_counts().max()
print(f'Country with max goals: {maxGoalsCntry} ({maxGoals})')

print("\n")
country='Russia'
totalGoalsByCntry = df['Country'][df.Country==country].value_counts().max()
print(f'Goals for {country} is: {totalGoalsByCntry}')

print("\n\n")
maxGoalsPlayer = df['Player'].value_counts().idxmax()
maxGoals = df['Player'].value_counts().max()
print(f'Player with max goals: {maxGoalsPlayer} ({maxGoals})')

print("\n")
player='Messi'
totalGoalsByPlyr = df['Player'][df.Player==player].value_counts().max()
print(f'Goals for {player} is: {totalGoalsByPlyr}')

bycountry = df[['Country', 'Player']].groupby('Country')

print("\n")
playrsforCountry=bycountry.filter(lambda x: x.Country.drop_duplicates() == 'Russia').Player.unique()
print(f'List of players for country {country} is {playrsforCountry}')

print("\n\n")
totalGoals = df['Country'].value_counts().sum()
print(f'total number of goals by all countries: {totalGoals}')

print("\n")
totalGoals = df['Time'][df.Time < 45].count()
print(f'total number of goals scored during 1st half: {totalGoals}')

print("\n")
totalGoals = df['Time'][(df.Time >= 45) & (df.Time < 90)].count()
print(f'total number of goals scored during 2nd half: {totalGoals}')

print("\n")
totalGoals = df['Time'][df.Time >= 90].count()
print(f'total number of goals scored during extra time: {totalGoals}')

print("\n")
totalGoalsByCountry=df['Country'].value_counts()
print(f'Total number of goals scored by each country: {totalGoalsByCountry}')

###############################################################################

cntry1 = random.choice(df['Country'])
cntry2 = random.choice(df['Country'])

totalGoalsByCntry1 = df['Country'][df.Country==cntry1].value_counts().max()
totalGoalsByCntry2 = df['Country'][df.Country==cntry2].value_counts().max()

print(f'Goals for randomly chosen countries {cntry1} and {cntry2} is: {totalGoalsByCntry1} and {totalGoalsByCntry2}')