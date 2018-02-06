# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def get_children(container,target):
        idx_list = []
 #       print(target,container)
        for idx,next in enumerate(container):
                if  next == target:
                        idx_list.append(idx);
                


        return idx_list 

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.heights = [0] * self.n 
                self.root  = self.parent.index(-1)
        def get_root(self):
                return self.parent.index(-1)

        def constructe_tree(self):
                parents=[-1]
								#find parents index




        def compute_height(self):
                # Replace this code with a faster implementation

                maxHeight = 0 ;
                for vertex in range(self.n):
                        if self.heights[vertex] !=0:
                                continue

                        height = 0 ; 
                        i = vertex ; 
                        while self.heights[i] != 0 and i != -1:
                                  height = height + 1 ; 
                                  i = self.parent[i] 
                                  # if self.heights[i] != 0:
                                         # height += self.heights[i];
                                         # break ;
                        height += self.heights[i]

                        maxHeight = max(maxHeight,height)
#                        print(maxHeight, height)
#                maxHeight = max(maxHeight,heighfor vertex in range(self.n):
                        i = vertex ; 
                        while self.heights[i] != 0 and i != -1:
                                  self.heights[i]= height; 
                                  height = height - 1;
                                  i = self.parent[i] 
                        # while i !=-1:
                                  # if self.heights[i] != 0:
                                         # break ;
                                  # self.heights[i]= height - 1  ; 
                                  # i = self.parent[i]


 #               print(maxHeight)
                return maxHeight



tree = TreeHeight()
#tree.read()
#root = int(tree.root)
tree.n = 3
tree.heights = [0]*tree.n
tree.parent = [-1,0,0]
#tree.parent = [-1,0,0,1]
print(tree.compute_height())
quit()
#quit()
#root = tree.get_root()
#print(root)
#tree.root = 1
#root=1
#print(tree.compute_height(root)+1)
#quit()
def main():
  tree = TreeHeight()
  tree.read()
  root = tree.root
  print(tree.compute_height())

threading.Thread(target=main).start()
