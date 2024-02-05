# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:23:51 2024

@author: Neno
"""
import movie_data_cleaning

#divide the strings in the Genre column into lists
movie_data_cleaning.movie_data['Genre'] = movie_data_cleaning.movie_data['Genre'].apply(lambda x: [genre.strip() for genre in x.split(',')])

#Combine genre into a one list
combine_genre = [genre for genre_list in movie_data_cleaning.movie_data['Genre'] for genre in genre_list]

#the number of unique genres
unique_genres = len(set(combine_genre))
print(unique_genres)