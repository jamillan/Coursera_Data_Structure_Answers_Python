# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def PrintData(self):
    print(self._data)

  def min_heap(self,i):
    l = 2*i+1;
    r = 2*i+2;
    smallest = i;
    if l < len(self._data) and self._data[l] < self._data[smallest]:
      smallest = l; 
			
    if r < len(self._data) and self._data[r] < self._data[smallest]:
      smallest = r; 

    if smallest !=i:
      self._data[i],self._data[smallest] = self._data[smallest],self._data[i]; 
      self._swaps.append((i,smallest))
      self.min_heap(smallest); 


  def GenerateSwaps(self):
    for i in range(len(self._data)//2,-1,-1):
      self.min_heap(i);


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    #self.PrintData()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
