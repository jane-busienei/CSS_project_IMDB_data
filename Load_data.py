# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:03:44 2024

@author: Neno
"""

import pandas as pd
#Loading data
movie_data = pd.read_csv("movie_dataset.csv")

print(movie_data)

# Data information
print(movie_data.info())
print(movie_data.describe())







