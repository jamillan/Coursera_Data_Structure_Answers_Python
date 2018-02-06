#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def inOrderTransversal(id,tree,results):
	if id == -1:
		return ;
#Go to left child
	l_id = tree[id][1]
	inOrderTransversal(l_id,tree,results) ;
	results.append(tree[id][0])
	r_id = tree[id][2]
	inOrderTransversal(r_id,tree,results) ;




def IsBinarySearchTree(tree):

  if len(tree) == 0: 
    return True ;
  results = []
  inOrderTransversal(0,tree,results)
  is_order = all(results[i] <= results[i+1] for i in range(len(results)-1))
  # Implement correct algorithm here
  return is_order


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
