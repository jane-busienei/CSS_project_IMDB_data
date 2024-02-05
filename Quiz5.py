# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:01:13 2024

@author: Neno
"""

import movie_data_cleaning 

#Filter movies released by director Christopher Nolan only
Nolan_release = movie_data_cleaning.movie_data[movie_data_cleaning.movie_data['Director'] == "Christopher Nolan"]

#count and print the number of movies relesed by director Christopher Nolan
Nolan_movie_count = len(Nolan_release)
print(Nolan_movie_count)