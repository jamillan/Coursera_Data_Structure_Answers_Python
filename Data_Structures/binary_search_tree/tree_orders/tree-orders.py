# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.iter =  0 ; 
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
			


  def inOrderTransversal(self,id):
    if id == -1: 
      return ;
	#Go to left child
    l_id = self.left[id]
    self.inOrderTransversal(l_id) ;
    self.result.append(self.key[id])
    r_id = self.right[id]
    self.inOrderTransversal(r_id) ;

	
  def inOrder(self):
    self.result = []
    self.inOrderTransversal(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    return self.result



  def preOrderTransversal(self,id):
    if id == -1: 
      return ;
	#Go to left child
    self.result.append(self.key[id])
    l_id = self.left[id]
    r_id = self.right[id]
    self.preOrderTransversal(l_id) ;
    self.preOrderTransversal(r_id) ;



  def preOrder(self):
    self.result = []
    self.preOrderTransversal(0)
    return self.result


  def posOrderTransversal(self,id):
    if id == -1: 
      return ;
	#Go to left child
    l_id = self.left[id]
    r_id = self.right[id]
    self.posOrderTransversal(l_id) ;
    self.posOrderTransversal(r_id) ;
    self.result.append(self.key[id])



  def postOrder(self):
    self.result = []
    self.posOrderTransversal(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
