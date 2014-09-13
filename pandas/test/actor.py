#ACTOR
from pandas import DataFrame
import  pandas as pd
ACTOR_n = ['id', 'fname', 'lname', 'gender']
path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBPerson.txt'

idn,fname,lname,gender = [],[],[],[]
with open(path) as f:
    for i, line in enumerate(f):                                                       
        fields = line.strip().split(",") 
        print i
        idn.append(fields.pop(0))
        fname.append(fields.pop(1))
        gender.append(fields.pop(-1))                                                
        lname.append(fields.pop(-1)) 
        
ACTOR_d = {'id':idn, 'fname':fname, 'lname':lname, 'gender':gender}
ACTOR1 = pd.DataFrame(ACTOR_d,columns = ACTOR_n )
ACTOR = ACTOR1.ix[2:]