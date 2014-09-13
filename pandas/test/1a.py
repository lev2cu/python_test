
from IPython.core.debugger import Tracer
import numpy as np
from pandas import Series, DataFrame, read_csv
import pandas as pd
import calendar



 
def movie():
    loca ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie.txt'
    MOVIE_n = ['id', 'name', 'year', 'rank']
    idn,rank,year,name = [],[], [], []
    with open(loca) as f:
        for i, line in enumerate(f):                                                    
            fields = line.strip().split(",")  
            idn.append(fields.pop(0))
            rank_ = fields.pop(-1)
            rank.append(rank_ if rank_ else np.nan)                                                
            year.append(fields.pop(-1))   
            nae = '{}'.format(",".join(fields))                                              
            name.append(nae)
    MOVIE_d = {'id':idn,'name': name,'year':year,'rank':rank}
    MOVIE1 = DataFrame(MOVIE_d,columns = MOVIE_n )
    return MOVIE1.ix[2:]

def actor():
    ACTOR_n = ['id', 'fname', 'lname', 'gender']
    loca ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBPerson.txt'
    print 'actor'
    idn,fname,lname,gender = [],[],[],[]
    with open(loca) as f:
        for i, line in enumerate(f):                                                       
            fields = line.strip().split(",") 
            idn.append(fields.pop(0))
            fname.append(fields.pop(1))
            gender.append(fields.pop(-1))                                                
            lname.append(fields.pop(-1)) 
    ACTOR_d = {'id':idn, 'fname':fname, 'lname':lname, 'gender':gender}
    ACTOR1 = DataFrame(ACTOR_d,columns = ACTOR_n )
    return ACTOR1.ix[2:]
    
def cast():
    CAST_n = ['pid','mid', 'role']
    loca ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBCast.txt'
    print 'cast'
    pid,mid,role = [],[],[]
    with open(loca) as f:
        for i, line in enumerate(f):                                                       
            fields = line.strip().split(",")     
            pid.append(fields.pop(0))
            role.append(fields.pop(1))
            mid.append(fields.pop(-1))            
    CAST_d = {'pid':pid, 'mid':mid, 'role':role} 
    df_CAST = DataFrame(CAST_d, columns = CAST_n)
   # print df_CAST.head()
    return df_CAST.ix[2:]
    
def director():
    DIRECTOR_n = ['id', 'fname', 'lname']
    loca ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBDirectors.txt'
    print 'dir'
    idn,fname,lname = [],[],[]
    with open(loca) as f:
        for i, line in enumerate(f):                                                       
            fields = line.strip().split(",")     
            idn.append(fields.pop(0))
            fname.append(fields.pop(1))
            lname.append(fields.pop(-1))             
    DIRECTOR_d = {'id':idn, 'fname':fname, 'lname':lname}
    DIRECTOR1 = pd.DataFrame(DIRECTOR_d,columns = DIRECTOR_n )
    return DIRECTOR1.ix[2:]
    
def mov_director():
    MOVIE_DIRECTOR_n= ['did', 'mid']
    loca ='/Applications/XAMPP/xamppfiles/htdocs/IMDB/IMDBMovie_Directors.txt'
    print 'mdir'
    MOVIE_DIRECTOR_1=read_csv(loca, names= ['did', 'mid'])
    return MOVIE_DIRECTOR_1.ix[2:]
    
def main():
    MOVIE = movie()
    ACTOR = actor()
    CAST = cast()
    print 'hello'
    DIRECTOR = director()
    MOVIE_DIRECTOR = mov_director()
  
    cast_1 = CAST.rename(columns={'mid':'id'}) 
    mov_cast = pd.merge(MOVIE,cast_1, on='id')    #CAST.mid refers to MOVIE.id 
    
    actor_1 = ACTOR.rename(columns={'id':'pid'})
    mov_cs_act = pd.merge(mov_cast,actor_1, on='pid')#CAST.pid refers to ACTOR.id
      
    mdirector_1 = MOVIE_DIRECTOR.rename(columns={'mid':'id'})
    mov_dir = pd.merge(MOVIE,mdirector_1, on='id')#MOVIE_DIRECTOR.mid refers to MOVIE.id
        
    director_1 = DIRECTOR.rename(columns={'id':'did'})
    mov_m_dir = pd.merge(mov_dir,director_1, on='did')#MOVIE_DIRECTOR.did refers to DIRECTOR.id
    
    mnY = int(MOVIE['year'].min())
    mxY = int(MOVIE['year'].max())
    year_count =(MOVIE['year'].value_counts()).sort_index()

    Myear =[]
    for i in range(len(year_count)):
        Myear.append(year_count[i:i+10].sum())
    ys = Series(Myear).idxmax()

    


    Tracer()()
      

#    
#    #1a. List all the actors who acted in at least one film in 2nd half of the 
#    #19th century and in at least one film in the 1st half of the 20th century
#    c19 = mov_cs_act.ix[(mov_cs_act['year'] >= '1850')&(mov_cs_act['year'] <'1900'), "pid"]
#    c20 = mov_cs_act.ix[(mov_cs_act['year'] >= '1900')&(mov_cs_act['year'] <'1950'), "pid"]    
#    c1920 = pd.merge(pd.DataFrame(c19).drop_duplicates(),pd.DataFrame(c20).drop_duplicates())
#    Actors = pd.merge(c1920,actor_1, on='pid')
#    print Actors.ix[:,1:3].head()
#   
#    
#    #1b. List all the directors who directed a film in a leap year
#    #    mov_cs_act.iloc[:,2]
#    #
#    #    calendar.isleap(mov_cs_act['year'])
#    # directors = mov_m_dir.ix[]
#  
#  
#    #2 List all the movies that have the same year as the movie 'Shrek (2001)', but a better rank
#    
#    shrek_y = MOVIE[MOVIE['name']=='Shrek (2001)']
#    s_mov = pd.merge(MOVIE[MOVIE['year'] == shrek_y.iloc[0,2]] ,MOVIE[MOVIE['rank'] > shrek_y.iloc[0,-1]], on = 'id',how = 'inner')
#    print s_mov.iloc[:,1]
#
#
#
#    #3 List first name and last name of all the actors who played in the movie 'Officer 444 (1926)'
#    
#    act_id = mov_cs_act[mov_cs_act['name'] == 'Officer 444 (1926)']
#    print act_id.ix[:,6:8]
#
#    #4 List all directors in descending order of the number of films they directed
#    
#    dir_c = mov_m_dir.groupby(['did','fname','lname']).size()
#    dir_c.order(ascending=False)
#
#   
#    #5 Find the film(s) with the largest cast
#    lcast = mov_cast.groupby('name').size()
#    print lcast.order(ascending=False)
    

    #6 Find all the actors who acted in films by at least 10 distinct directors
    #(i.e. actors who worked with at least 10 distinct directors).
    
    a1 = mov_cs_act['pid']
    b1 = pd.merge(pd.DataFrame(a1).pd.DataFrame(mov_m_dir))
    Actors = pd.merge(b1,actor_1, on='pid')

    #7Find all actors who acted only in films before 1960.
    a60 = mov_cs_act.ix[(mov_cs_act['year'] < '1960'), "pid"]
    Actors = pd.merge(a60,actor_1, on='pid')
    print Actors.ix[:,1:3].head() 
    
    #8 Find the films with more women actors than men.
    cast_id = mov_cs_act['id'].groupby(mov_cs_act['gender']).count
    
    #9 For every pair of male and female actors that appear together in some film, find the total number of films in which they appear together. Sort the answers in decreasing order of the total number of films.
# 
#(8') For every actor, list the films he/she appeared in their debut year. Sort the results by last name of the actor.
#    
    
    
    
    
    
    
if __name__ == "__main__":
      main()
      