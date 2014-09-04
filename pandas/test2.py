from pandas import Series, DataFrame
import pandas as pd

df1 = DataFrame({'rkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = DataFrame({'lkey': ['a', 'b', 'd'], 'data2': range(3)})

# different column names
data = pd.merge(df1, df2,left_on = 'rkey', right_on='lkey');

print data