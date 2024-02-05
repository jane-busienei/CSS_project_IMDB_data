# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:39:10 2024

@author: Neno
"""

import movie_data_cleaning 
import pandas as pd

#divide the strings in the Actors column into lists
movie_data_cleaning.movie_data['Actors'] = movie_data_cleaning.movie_data['Actors'].apply(lambda x: [actor.strip() for actor in x.split(',')])

#Combine actors into a one list
combine_actors = [actor for actors_list in movie_data_cleaning.movie_data['Actors'] for actor in actors_list]

# Create a Pandas Series from the list of actors
actors_series = pd.Series(combine_actors)

# Find the most common actor
most_common_actor = actors_series.mode().iloc[0]
print(most_common_actor)