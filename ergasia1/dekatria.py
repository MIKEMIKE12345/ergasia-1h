
from itertools import combinations 
def maxDistance(p,m):
 maxj = -1 
 for y in range(1,len(p)):
   comb = combinations(p, y) 
   for j in list(comb): 
         sum=0
         for z in list(j): 
                sum+= z 
                if sum <= m:     
                 maxj = max(sum, maxj)  
 w = 0
 for k in list(p):
     w = w + k

 maxj = max(w, maxj)
 print (maxj)


 
