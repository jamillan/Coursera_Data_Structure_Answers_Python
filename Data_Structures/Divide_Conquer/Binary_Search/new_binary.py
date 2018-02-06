# Uses python3
import sys
#from math import *




def BinarySearch(a,elem=None, lo_val =0 , hi_val = None):
 if hi_val is None:
  hi_val = len(a);

 #Create loop through low and high values
 while lo_val < hi_val:
  #find midpoint
  mid_val = (lo_val + hi_val)//2
  midval =a[mid_val]
	#is target below midpoint
  if midval < x:
   lo_val = mid_val +1 ;
	#is target above midpoint

	#if that is not the cse we found possibly the target
  elif midval > x:
   hi_val = mid_val 
  else:
   return mid_val

 #ok nof target not found
 return -1;



if __name__ == '__main__':

 #x= 5
 #test = [1,2,3,4]
 #print(BinarySearch(a=test, elem = x))
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
  print(BinarySearch(a=a, elem = x), end= ' ')






 
