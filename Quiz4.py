# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:29:56 2024

@author: Neno
"""
import movie_data_cleaning 

#Filter movies released in 2016 only
release_2016 = movie_data_cleaning.movie_data[movie_data_cleaning.movie_data['Year'] == 2016]

#count and print the number of movies relesed in 2016
movies_release_2016 = len(release_2016)
print(movies_release_2016)
