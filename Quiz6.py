# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:06:21 2024

@author: Neno
"""

import movie_data_cleaning 

#Filter movies with at least 8.0 rating
rating_8 = movie_data_cleaning.movie_data[movie_data_cleaning.movie_data['Rating'] >= 8.0]

#count and print the number of movies with at least 8.0 rating
rating_8_movies = len(rating_8)
print(rating_8_movies)
