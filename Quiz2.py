# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:56:42 2024

@author: Neno
"""

import movie_data_cleaning

#Calculating the average of the revenue
Revenue_average = movie_data_cleaning.movie_data["Revenue(Millions)"].mean()
print(Revenue_average)