from scipy.sparse import coo_matrix
import  pandas as pd

path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie3.txt'
idn = []

with open(path) as f:
    for i, line in enumerate(f):
        for fields in line.strip().split(",") :
            idn = fields.pop(0) 
   #         id.append(idn)
 
        ## Get unambiguous fields.                                            
        #id = fields.pop(0)                                                   
        #rank = fields.pop(-1)                                                
        #year = fields.pop(-1)                                                
        ## Surround name with quotes.                                         
        #name = '"{}"'.format(",".join(fields)) 
        #print("{},{},{},{}".format(id, name, year, rank)) 