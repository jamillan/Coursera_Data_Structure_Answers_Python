# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        #print(self.nodes) 
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.start_times = [None] * len(self.jobs)
        self.ids = [i for i in  range(self.num_workers) ]
        self.nodes = [0] * self.num_workers
        self.assigned_workers = [None] * len(self.jobs)

        for i in range(len(self.jobs)):

          self.start_times[i] =  int(self.nodes[0])
          self.assigned_workers[i] =  int(self.ids[0])
          #print(self.ids[0],self.nodes[0])
          self.nodes[0] =  self.nodes[0] + self.jobs[i]
#          print("nodes 1: ",self.nodes) 
 #         print("ids 1: ",self.ids) 
          self.sift_down_nodes(0)
  #        print("nodes 2: " ,self.nodes) 
   #       print("ids 2: " ,self.ids) 
					

          #for j in range(self.num_workers):
           # if next_free_time[j] < next_free_time[next_worker]:
            #  next_worker = j
    def sift_down_nodes(self,i):
        # TODO: replace this code with a faster algorithm.
        l = 2*i + 1; 
        r = 2*i + 2; 
        smallest = i; 
        if l < len(self.nodes) and self.nodes[l] <= self.nodes[smallest]: 

          if self.nodes[l] < self.nodes[smallest] :
            smallest = l;

          if self.nodes[l] == self.nodes[smallest] :
            if self.ids[l] < self.ids[smallest]:
              smallest = l 

        if r < len(self.nodes) and self.nodes[r] <= self.nodes[smallest]: 

          if self.nodes[r] < self.nodes[smallest] :
            smallest =  r;

          if self.nodes[r] == self.nodes[smallest] :
            if self.ids[r] < self.ids[smallest]:
              smallest = r 
          



        if smallest != i:  
          self.nodes[i],self.nodes[smallest] = self.nodes[smallest],self.nodes[i];
          self.ids[i],self.ids[smallest] = self.ids[smallest],self.ids[i];
          self.sift_down_nodes(smallest);




    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

