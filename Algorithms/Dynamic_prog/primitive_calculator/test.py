# Uses python3
import sys
def get_sequence(n):
    n = int(n)
    my_sequence = []
    memo = [0]*(n+1)
		#create memo table with optimal sequence


    for i in range(1,len(memo)):
        memo[i] = memo[i-1] + 1
        if (i%2 == 0):
            memo[i] = min(1+memo[i//2], memo[i])
        if (i%3 == 0):
            memo[i] = min(1+memo[i//3], memo[i])

    #ok now find optimal sequence
    while (n>1):
        my_sequence.append(n)
        if (memo[n-1] == memo[n]-1):
            n = n-1

        elif (n%2 == 0 and (memo[n//2] == memo[n]-1)):
            n = n//2		

        elif (n%3 == 0 and (memo[n//3] == memo[n]-1)):
        #elif (n%3 == 0 ):
            n = n//3


    my_sequence.append(1)
    return reversed(my_sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(get_sequence(n))
print(len(sequence) - 1)
for x in sequence:
 print(x, end=' ')
