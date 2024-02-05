# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:32:54 2024

@author: Neno
"""

import movie_data_cleaning 

#number of movies made in 2006
movies_06 = len(movie_data_cleaning.movie_data[movie_data_cleaning.movie_data['Year'] == 2006])

#number of movies made in 2016
movies_16 = len(movie_data_cleaning.movie_data[movie_data_cleaning.movie_data['Year'] == 2016])

#percentage increase
percentage_increase = ((movies_16 - movies_06) / movies_06) * 100
print(percentage_increase)