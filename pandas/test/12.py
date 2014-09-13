mnY = int(MOVIE['year'].min())
mxY = int(MOVIE['year'].max())
year_count =(MOVIE['year'].value_counts()).sort_index()

Myear =[]
for i in len(year_count):

    year_count = year_count[i-1:i+9].sum()
    Myear.append(year_count)
    Myear.max
    

    #ye = (MOVIE['year']>=mnY)  & (MOVIE['year']<=mnY+10)

    #my = ((m['year'] >= 'i+1') & (m['year']<=i+1) ).value_counts()
