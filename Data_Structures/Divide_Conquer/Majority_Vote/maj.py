# Uses python3
import sys
from random import shuffle




def get_majority_element(a):
# if side == "left":
 # print("rec: " + str(j))
 n = len(a)
 #if side == "left":
  #print("size " + str(n))
 if n == 1:
  #print("doing " + str(side))
  return int(a[0]);
	
# if n == 0:
#  raise RuntimeError("boo");


 k = int(n/2)
# if side == "left":
# print(a[:k])
# print(a[k:])
 elem_left = get_majority_element(a[:k])
 elem_right = get_majority_element(a[k:])
# if j == 0:
 # print(elem_left)
 # print(elem_right)
 # quit() 

 if elem_left == elem_right:
  return elem_left;

 lcount = 0;
 for i in a:
  if int(i) == elem_left:
   lcount +=1;

 rcount = 0;
 for i in a:
  if int(i) == elem_right:
   rcount +=1;

 if lcount > (k):
  return elem_left;

 if rcount > (k):
  return elem_right;

 else:
  return -1;



#m = [2,3,9,3,3,3,2]
#shuffle(m)
#print(m)
#print(getMajority(m))

if __name__ == '__main__':
 input = sys.stdin.read()
 n , *a = list(map(int,input.split()))
 if get_majority_element(a) != -1:
  print(1)
 else:
  print(0) 
