# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:35:30 2024

@author: Neno
"""

import movie_data_cleaning

#Finds the row with the highest value in a specific column
highest_rated = movie_data_cleaning.movie_data['Rating'].idxmax()

#Retrieve the entire row
highest_rated_movie = movie_data_cleaning.movie_data.loc[highest_rated]
print(highest_rated_movie)