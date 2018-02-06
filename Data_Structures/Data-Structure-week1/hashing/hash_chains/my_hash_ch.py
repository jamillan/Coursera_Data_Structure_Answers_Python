# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.buckets = [dict() for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
            ans = (ans + self._prime)% self._prime 
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            str_s = self.buckets[ query.ind].keys();
            str_s = list(str_s)
            str_s = str_s[::-1]
            self.write_chain(str_s)

        else:

            if query.type == 'add':

                cur_bucket = self._hash_func(query.s)
                try:
                    tmp_id = self.buckets[cur_bucket][query.s]
                except KeyError:
                    self.buckets[cur_bucket][query.s] = 1;
            #    print(self.buckets) 

            elif query.type == 'find':
                cur_bucket = self._hash_func(query.s)
                try:
                    counts =self.buckets[cur_bucket][query.s]
                except KeyError:
                    cur_bucket=-1
                self.write_search_result(cur_bucket != -1)

            else:
                cur_bucket = self._hash_func(query.s)
                try:
                    counts =self.buckets[cur_bucket].pop(query.s)
                except KeyError:
                    pass
										


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
