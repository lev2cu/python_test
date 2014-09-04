from pandas import Series, DataFrame
import pandas as pd

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

#outer join

data = pd.merge(df1, df2, how = 'outer')

print data