
from pandas import DataFrame
import  pandas as pd
CAST_n = ['pid','mid', 'role']
path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBCast.txt'
pid,mid,role = [],[],[]
with open(path) as f:
        for i, line in enumerate(f):                                                       
            fields = line.strip().split(",")     
            pid.append(fields.pop(0))
            mid.append(fields.pop(1))
            role.append(fields.pop(-1)) 
            
CAST_d = {'pid':pid, 'mid':mid, 'role':role}
df_CAST = DataFrame(CAST_d, columns = CAST_n)
CAST = df_CAST.ix[2:]