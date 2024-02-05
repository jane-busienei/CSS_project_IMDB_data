# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:47:02 2024

@author: Neno
"""
import movie_data_cleaning 

Year_movie_grouping = movie_data_cleaning.movie_data.groupby('Year')

#average rating for each group
average_ratings = Year_movie_grouping['Rating'].mean()

#the year with the highest average rating
highest_rating_year = average_ratings.idxmax()
print(highest_rating_year)


