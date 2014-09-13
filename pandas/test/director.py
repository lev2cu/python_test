
from pandas import DataFrame
import  pandas as pd
DIRECTOR_n = ['id', 'fname', 'lname']
path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBDirectors.txt'

idn,fname,lname = [],[],[]
with open(path) as f:
    for i, line in enumerate(f):                                                       
        fields = line.strip().split(",") 
 
        idn.append(fields.pop(0))
        fname.append(fields.pop(1))
        lname.append(fields.pop(-1)) 
        
DIRECTOR_d = {'id':idn, 'fname':fname, 'lname':lname}
DIRECTOR1 = pd.DataFrame(DIRECTOR_d,columns = DIRECTOR_n )
DIRECTOR = DIRECTOR1.ix[2:]