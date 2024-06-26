# -*- coding: utf-8 -*-
"""Copie de prep_exam_seaborn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xyYSfj7ReCp1HfAZrEt9ki_30rHlEjsi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_netflix=pd.read_csv('netflix_titles.csv')
df_netflix.listed_in.head(30)

sns.countplot('type',data=df_netflix)

df2=pd.read_csv('IMDB_parental_guide.csv')
df2

df.shape

df.columns

all_content=df2.merge(df_netflix,right_on='title',left_on='primaryTitle')

all_content['is action']=all_content['listed_in'].str.contains('Action')

all_content['is action']=all_content['listed_in'].apply(lambda x: 'Action' in x)

all_content['is action'].head(50)

all_content['is action'].value_counts()

all_movies= all_content[all_content['type'] == 'Movie']

all_movies=pd.DataFrame(all_movies.primaryTitle)
all_movies['title']=all_movies['primaryTitle']
all_movies.drop(columns=['primaryTitle'])

df

df_netflix.loc[df_netflix.type=='Movie']

movies= all_content.loc[all_content['type'] == 'Movie']
movies



movies['duration'] = movies.duration.str.replace('min','',regex=True)

movies = movies.dropna(subset=["duration"])
movies.duration = movies.duration.astype(int)

all_movies['duree']=movies.duration

len(movies.duration)

all_movies['is action']=all_content['is action']

sns.catplot('is action','duree',kind='box',width=0.3,data=all_movies)
plt.ylim(30,180)

all_content['is action']

all_content.duree

action_movies = all_movies[all_movies['is action']==True]['duree']
non_action_movies = all_movies[all_movies['is action']==False]['duree']
# Créer le boxplot
plt.boxplot([action_movies, non_action_movies], labels=['Action', 'Non-Action'])
plt.ylabel('Durée (minutes)')
plt.show()

all_content.country

action_movies_usa = all_content[(all_content["is action"] == True) & (all_content["country"] == "United States") & (all_content['duree']<160)]

duree=action_movies_usa.duree

all_content

sns.relplot(duree,all_content.averageRating	)

all_content.director
S=pd.Series(all_content.director)
ser=S.str.split(',',expand=True).stack().reset_index(drop=True)

series=ser.value_counts()
top_8=series.head(8)

sns.barplot(x=top_8.values,y=top_8.index,orient='h')

g=pd.to_datetime(all_content.date_added)
g

g