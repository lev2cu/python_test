
from pandas import Series, DataFrame
import pandas as pd

df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'tatq':[3,1,5,1,2,3]})

#CREATe dummy data
df_dummy = pd.get_dummies(df['key'])

# join dummy data
df_wit_dummy = df[['tatq']].join(df_dummy)

print df_wit_dummy