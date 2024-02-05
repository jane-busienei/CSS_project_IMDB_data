# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:15:21 2024

@author: Neno
"""

import movie_data_cleaning 

#Filter movies released by director Christopher Nolan only
Nolan_movies = movie_data_cleaning.movie_data[movie_data_cleaning.movie_data['Director'] == "Christopher Nolan"]

#median rating of movies directed by Christopher Nolan
Nolan_rating_median = Nolan_movies['Rating'].median()
print(Nolan_rating_median)