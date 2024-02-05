# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:46:14 2024

@author: Neno
"""

import movie_data_cleaning
import seaborn as sns
import matplotlib.pyplot as plt

#include only numeric column
movie_numeric_data = movie_data_cleaning.movie_data.select_dtypes(include = ['float','int'])

#Correlate numerical features
movie_correlation = movie_numeric_data.corr()
print(movie_correlation)

#Visualize using heatmap
sns.heatmap(movie_correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix Heatmap")
plt.show()

