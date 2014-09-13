# -*- coding: utf-8 -*-

import pandas as pd

MOVIE_n = ['id', 'name', 'year', 'rank']

ACTOR_n = ['id', 'fname', 'lname', 'gender']
ACTOR = pd.read_table('/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBPerson.txt',sep = ',',header =None,names = ACTOR_n)

DIRECTOR_n = ['id', 'fname', 'lname']
CAST_n = ['pid','mid', 'role']
MOVIE_DIRECTOR_n= ['did', 'mid']

MOVIE = pd.read_table('/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie.txt',sep = ',',header =None,names = MOVIE_n)
CAST = pd.read_table('/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBCast.txt',sep = ',',header =None,names = CAST_n)
DIRECTOR = pd.read_table('/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBDirectors.txt',sep = ',',header =None,names = DIRECTOR_n)
MOVIE_DIRECTOR = pd.read_table('/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie_Directors.txt',sep = ',',header =None,names = MOVIE_DIRECTOR_n)



