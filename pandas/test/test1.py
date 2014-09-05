from pandas import Series, DataFrame
import pandas as pd


df1 = DataFrame({'key': ['a', 'b', 'a', 'b' , 'c'], 'data1': range(5)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

data = pd.merge(df1,df2, on = 'key')
#many to one situation 
print data