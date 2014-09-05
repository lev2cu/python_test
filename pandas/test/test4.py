from pandas import Series, DataFrame
import pandas as pd

df1 = DataFrame({'key': ['b', 'b', 'a', 'c'], 'data1': range(4)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

#many to many

data = pd.merge(df1, df2, on='key', how = 'outer')
#
#inner
#data = pd.merge(df1, df2, on='key', how = 'inner')
#left
#data = pd.merge(df1, df2, on='key', how = 'left')
#right
#data = pd.merge(df1, df2, on='key', how = 'right')

print data