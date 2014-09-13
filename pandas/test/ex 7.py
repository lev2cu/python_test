
from IPython.core.debugger import Tracer
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

def director():
    DIRECTOR_n = ['id', 'fname', 'lname']
    path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBDirectors.txt'
    print 'dir'
    idn,fname,lname = [],[],[]
    with open(path) as f:
        for i, line in enumerate(f):                                                       
            fields = line.strip().split(",")     
            idn.append(fields.pop(0))
            fname.append(fields.pop(1))
            lname.append(fields.pop(-1))             
    DIRECTOR_d = {'id':idn, 'fname':fname, 'lname':lname}
    DIRECTOR1 = pd.DataFrame(DIRECTOR_d,columns = DIRECTOR_n )
    return DIRECTOR1.ix[2:]
    
    
def main():
      #     DIRECTOR = director()
        
        MOVIE_DIRECTOR = director()
        Tracer()()
    
if __name__ == "__main__":
      main()