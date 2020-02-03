from random import*
import random
import json
import pdb
scorecard_1={}
scorecard_2={}
scorecard={}
matches=[]
matches_last_2=[]
matches_top_2=[]
semi_q={}


    
def match_function(tlist):
    for i in range (0,len(tlist)):
        match=tlist[i]
        for j in range(i+1,len(tlist)):
            match2=tlist[j]
            (matches.append((match,match2)))
    #print(matches)
    for match in matches:
        a=random.randint(0,1)
        #print(f" the match between teams : {match} : the match winner : {match[a]} : sorecard : {randint(0,1)}")
        match=(f"{match[a]}") 
        result=(f"{int(randint(0,1))}")
        scorecard[match]=result
    print(scorecard)
    
    
    return scorecard
    
def sort_function(quali1,quali2):
    #d=quali1
    #e=quali2
    semi={}
    semi_list=[]
    for (key) in quali1:
        if (key)in  quali2:
            semi[(key)]=int(quali1[(key)])+int(quali2[(key)])
    #print(semi)
    top_4=sorted(semi.items(),key=lambda x:x[1])
    print("the top 4 teams : ",top_4)
    #print(top_4[4:9:1])
    for i in (top_4[4:9:1]):
        (semi_list.append(f"{i[0]}"))
    print(semi_list)
    
    return semi_list
   
    
  
def semi_function(slist):
    final_2=[]
    
    top_last={}
    top_first={}
    for i in range (0,len(slist)):
        match3=slist[i]
        for j in range(i+1,2):
            match4=slist[j]
            (matches_last_2.append((match3,match4)))
    print("the match between last teams in point table :",matches_last_2)
    for i in range (2,len(slist)):
        match1=slist[i]
        for j in range(i+1,len(slist)):
            match2=slist[j]
            (matches_top_2.append((match1,match2)))
    print("the match between top teams in leagues :",matches_top_2)
    for match in matches_last_2:
        a=random.randint(0,1)
        #print(f"{match} :{match[a]} : {randint(1,2)}")
        match=(f"{match[a]}") 
        result=(f"{int(randint(0,1))}")
        top_last[match]=result
        final_2.append((top_last))
    print("match between  last  2 teams and winner is : " ,top_last)
        
    for match in matches_top_2:
        a=random.randint(0,1)
        #print(f"{match} :{match[a]} : {randint(0,1)}")
        match=(f"{match[a]}") 
        result=(f"{int(randint(0,1))}")
        top_first[match]=result
        final_2.append((top_first))
    print("match between first 2 teams  winner is:" ,top_first)
    
    return final_2
   
    
    
    
    
def final_winner(dlist):
    e=dlist[0]
    f=dlist[1]
    team1=dict(e)
    team2=dict(f)
    final_teams=[]
    final_match=[]
    for key,value in (team1.items()):
        print(final_teams.append(key))
    for key,value in (team2.items()):
        print(final_teams.append(key))
    print(final_teams)
    n=len(final_teams)
    
    for i in range(0,n):
        team_1=final_teams[i]
        for j in range(i+1,n):
            team_2=final_teams[j]
            final_match.append((team_1,team_2))
    print(final_match)
    for match  in final_match:
        a=random.randint(0,1)
        points=(f" the final match between :  {match} : the match winner is : {match[a]} : sorecard : {randint(0,1)}")
        
        print(points)
    
        
        
            
        
   
     
    
    
        
    
    
   
    
    

    
    
 
    
    
    
def main():
    team1=["india","nambia","australlia","newzeland","southafrica","srilanka","westindies","england"]
    qualifiers_1=match_function(team1)
    qualifiers_2=match_function(team1)
    z=sort_function(qualifiers_1,qualifiers_2)
    semis=semi_function(z)
    final_winner(semis)
    
    
   
    
    
    


    
    
if (__name__ == "__main__"):
    main()

    

    

    
    
    
    
    
    
       
            
    

	
		
	