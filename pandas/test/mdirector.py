from pandas import DataFrame
import  pandas as pd

#MOVIE_DIRECTOR_n= ['did', 'mid']
path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie_Directors.txt'

did,mid = [],[]
with open(path) as f:
    for i, line in enumerate(f):                                                       
        fields = line.strip().split(",") 
 
        did.append(fields.pop(0))
        mid.append(fields.pop(1))
        
        MOVIE_DIRECTOR = {'did':did, 'mid':mid}
        df_MOVIE_DIRECTOR = DataFrame(MOVIE_DIRECTOR)