# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            try:
                tmp_nbr = contacts[cur_query.number]
            except KeyError: # otherwise, just add it
                contacts[cur_query.number] = cur_query.name
                continue; 


            contacts[cur_query.number] = cur_query.name


        elif cur_query.type == 'del':
            try:
                tmp_name = contacts.pop(cur_query.number)
            except KeyError: # otherwise, just add it
                pass

        else:
            try:
                response = contacts[cur_query.number]
            except KeyError: # otherwise, just add it
                response = 'not found'
         

            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

