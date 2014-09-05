import numpy as np
from pandas import Series,DataFrame
import pandas as pd

np.random.seed(12345)
data = DataFrame(np.random.randn(1000, 4))
print data.describe()

#cap values outside the interval -3 to 3
data[np.abs(data)>3] = np.sign(data)*3
