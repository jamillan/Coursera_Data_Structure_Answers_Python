# Uses python3
import sys
#from math import *




def BinarySearch(a,elem=None,j=0,side="right"):
# if elem == None:
 # raise RuntimeError("define targeted element for search");
# if side == "left":
 # print("rec: " + str(j))
 n = len(a)
	
 if n == 0:
  raise RuntimeError("boo");


 if n == 1:
  Match = -1 ;
  if a[0] == elem:
   Match = j;
  return Match ;


 if n == 2:

  Match = -1 ;

  if a[0] == elem:
   Match = (j);
 #  print("d")

  if a[1] == elem:
   Match = (j+1);
#   print("d1")

  return Match; 

 k = int(n/2)
# if side == "left":

 elem_left = BinarySearch(a[:k],j=j ,elem = elem ,side="left")
 elem_right = BinarySearch(a[k:],j=j+k,elem = elem)
# print(elem_left,elem_right)
# if j == 0:
 # print(elem_left)

 if elem_left == elem_right:
  return elem_left;

 if elem_left != -1:
  return elem_left;

 if elem_right != -1:
  return elem_right;
  

 else:
  return -1;




if __name__ == '__main__':

# x= 2
 #test = [1,2,3]
 #print(BinarySearch(a=test,j=0, elem = x))
 #quit()
 input = sys.stdin.read()
 data = list(map(int, input.split()))
 n = data[0]
 m = data[n + 1]
 a = data[1 : n + 1]
 #print(data)
 #print(m)
# print(data[n+2:])
 #quit()
 for x in data[n + 2:]:
  print(BinarySearch(a=a,j=0, elem = x), end= ' ')






 
