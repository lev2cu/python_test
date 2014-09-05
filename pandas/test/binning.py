import pandas as pd


ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

# function cut

data = pd.cut(ages,bins,labels = group_names)
print data