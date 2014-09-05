
from pandas import Series, DataFrame
import pandas as pd

left = DataFrame({'k1': ['sd','we', 'er'], 'k2': ['sd','iu','we'], 'lval': [1,2,3]})
right = DataFrame({'k1':['we','er'], 'k2': ['iu', 'sd'], 'rval':[4,5]})

data = pd.merge(left,right,on='k2')

print data