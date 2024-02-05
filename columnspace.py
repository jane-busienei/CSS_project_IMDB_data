# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:41:43 2024

@author: Neno
"""

import Load_data

#remove spaces in column names
Load_data.movie_data.columns = Load_data.movie_data.columns.str.replace(' ', '')

#list column names
col_names = Load_data.movie_data.columns.tolist()
Load_data.movie_data.reset_index(inplace=True)
print(col_names)
