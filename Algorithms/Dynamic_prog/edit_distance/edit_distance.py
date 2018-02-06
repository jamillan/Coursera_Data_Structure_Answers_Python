# Uses python3
def edit_distance(s1,s2):
 m = len(s1) + 1
 n = len(s2) + 1 

 #memo distance
 distance = {}
 #initialize to zero row 0 and col 0 
 for i in range(m):distance[i,0]=i
 for j in range(n):distance[0,j]=j
 
 # ok loop through them strings and calculate penalization

 for i in range(1,m):
  for j in range(1,n):

# Cost of penalization 
   cost = 0 ;
   if s1[i-1] !=s2[j-1]:
    cost = 1;

   distance[i,j] = min(distance[i, j-1]+1, distance[i-1, j]+1, distance[i-1, j-1]+cost)

 return distance[i,j]




if __name__ == "__main__":
 print(edit_distance(input(), input()))
