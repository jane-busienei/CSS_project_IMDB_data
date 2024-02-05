# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:43:48 2024

@author: Neno
"""
import pandas as pd
#Loading data
movie_data = pd.read_csv("movie_dataset.csv")

#remove spaces in column names
movie_data.columns = movie_data.columns.str.replace(' ', '')

#Display all rows
#pd.set_option('display.max_rows',None)

#Detect columns with missing values using isna() which return true for missing values
nans_column = movie_data.columns[movie_data.isna().any()].tolist()
print(nans_column)

#Linear interpolation to estimate missing values based on the v
movie_data['Metascore'] = movie_data['Metascore'].interpolate()

#Getting the Revenue(Millions) mean
Revenue_mean = movie_data["Revenue(Millions)"].mean()

#Filling the nans with mean
movie_data["Revenue(Millions)"].fillna(Revenue_mean, inplace = True)

#Checking for duplicated data
duplicated_rows = movie_data[movie_data.duplicated()]

