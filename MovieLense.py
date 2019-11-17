#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 5 14:46:05 2019

@author: mahya
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

rating_data = pd.read_csv('ratings.csv')
movie_names = pd.read_csv('movies.csv')
movie_data = pd.merge(rating_data,movie_names, on='movieId')

rating_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
rating_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
#
#plt.figure(figsize=(8, 6))
#plt.rcParams['patch.force_edgecolor'] = True
#rating_mean_count['rating_counts'].hist(bins=50)
#
#plt.figure(figsize=(8,6))
#plt.rcParams['patch.force_edgecolor'] = True
#rating_mean_count['rating'].hist(bins=50)
#
#plt.figure(figsize=(8,6))
#plt.rcParams['patch.force_edgecolor'] = True
#sns.jointplot(x='rating', y='rating_counts', data=rating_mean_count, alpha=0.4)

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')
forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']

movies_like_forrestgump = user_movie_rating.corrwith(forrest_gump_ratings)
corr_forrestgump = pd.DataFrame(movies_like_forrestgump, columns=['Correlation'])
corr_forrestgump.dropna(inplace=True)
print(corr_forrestgump.sort_values('Correlation', ascending=False).head())
corr_forrestgump = corr_forrestgump.join(rating_mean_count['rating_counts'])