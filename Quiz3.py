# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 09:47:37 2024

@author: Neno
"""

import movie_data_cleaning 
#filter the years from 2015 to 2017
extract_year = movie_data_cleaning.movie_data[(movie_data_cleaning.movie_data["Year"] >= 2015) & (movie_data_cleaning.movie_data["Year"] <= 2017)]

#the average revenue of movies from 2015 to 2017
mean_revenue1 = extract_year["Revenue(Millions)"].mean()
print(mean_revenue1)