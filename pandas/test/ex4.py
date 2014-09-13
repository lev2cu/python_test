#movie.txt
from pandas import DataFrame
import  pandas as pd

path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie3.txt'

idn,rank,year,name = [],[], [], []
with open(path) as f:
    for i, line in enumerate(f):                                                       
        fields = line.strip().split(",") 
 
        idn.append(fields.pop(0))
        rank.append(fields.pop(-1))                                                
        year.append(fields.pop(-1))   
        nae = '{}'.format(",".join(fields))                                              
        name.append(nae)
        
        data = {'id':idn,'name': name,'year':year,'rank':rank}
        df = DataFrame(data)
        df1 = df.ix[2:]
    