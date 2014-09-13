
from pandas import  Series, DataFrame
import  pandas as pd

#movie.txt
path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie3.txt'

#fi = open(path)
#
#for line in fi:                                                           
#        fields = line.strip().split(",")   
#        
    #    with open(path) as f:
    #for i, line in enumerate(f):                                                       
    #    fields = line.strip().split(",") 

df = pd.read_csv(path, index_col=False, header=0);
serie = df.transpose()[0] 