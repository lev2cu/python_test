
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

mnames = ['movie_id', 'title', 'genres']

movies = pd.read_table('/Users/SJ/gHub/pydata-book/ch02/movielens/movies.dat', sep ='::', header = None, names = mnames)

genre_iter = (set(x.split('|')) for x in movies.genres)
genres = sorted(set.union(*genre_iter))
dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)
