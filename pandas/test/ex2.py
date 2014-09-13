
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

path ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie3.txt'


friends = open(path).readlines()
print friends[3].strip()