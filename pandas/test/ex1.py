
from pandas import  Series, DataFrame
import  pandas as pd

#movie.txt
path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie3.txt'
DataFrame.from_csv(path, header=0, sep=',', index_col=0)
fi = open(path)

for line in fi:                              
                                 
        fields = line.strip().split(",")                                     

        # Get unambiguous fields.                                            
        id = fields.pop(0)                                                   
        rank = fields.pop(-1)                                                
        year = fields.pop(-1)                                                
        # Surround name with quotes.                                         
        name = '"{}"'.format(",".join(fields)) 
        print("{},{},{},{}".format(id, name, year, rank)) 
        
        