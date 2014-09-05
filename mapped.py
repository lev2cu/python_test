
from pandas import Series, DataFrame
import pandas as pd

data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
meat_to_animal = { 'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow', 'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon'}

#The map method on a Series accepts a function or dict-like object containing a mapping,(case sensitive)
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print data
print data['animal']

# map with function
maped = data['food'].map(lambda x: meat_to_animal[x.lower()])
print maped