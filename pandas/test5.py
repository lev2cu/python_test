
from pandas import Series, DataFrame
import pandas as pd

left = DataFrame({'k1': ['sd','we', 'er'], 'k2': ['df','iu','ew'], 'lval': [1,2,3]})
right = DataFrame({'k1':['rt','sd'], 'k2': ['iu', 'iu'], 'rval':[4,5]})

#multiple keys: pass a list of column names -> on=['key1', 'key2'],
data = pd.merge(left,right,on=['k1','k2'], how = 'outer')

print data