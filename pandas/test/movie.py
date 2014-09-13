
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie.txt'
MOVIE_n = ['id', 'name', 'year', 'rank']
idn,rank,year,name = [],[], [], []
with open(path) as f:
    for i, line in enumerate(f):                                                       
        fields = line.strip().split(",") 
 
        idn.append(fields.pop(0))
        rank_ = fields.pop(-1)
        rank.append(rank_ if rank_ else np.nan)                                                
        year.append(fields.pop(-1))   
        nae = '{}'.format(",".join(fields))                                              
        name.append(nae)
        
        print i
MOVIE_d = {'id':idn,'name': name,'year':year,'rank':rank}
MOVIE1 = pd.DataFrame(MOVIE_d,columns =MOVIE_n )
MOVIE = MOVIE1.ix[2:]

    