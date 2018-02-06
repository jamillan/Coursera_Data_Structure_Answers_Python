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
	results.append([tree[id][0],id])
	r_id = tree[id][2]
	inOrderTransversal(r_id,tree,results) ;




def IsBinarySearchTree(tree):

  if len(tree) == 0: 
    return True ;
  results = []
  inOrderTransversal(0,tree,results)
  is_order = True	
  for i in range(len(results)-1):
    diff = results[i+1][0] - results[i][0] 
    if diff < 0:
      is_order = False;

    if diff == 0:
      cur_node = results[i+1][1]
      cur_node_key = tree[cur_node][0]
      l_child = tree[cur_node][1] 
      if l_child != -1:
        l_node_key = tree[l_child][0] 
        if cur_node_key <= l_node_key: 			
          is_order = False ;  
      			
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
