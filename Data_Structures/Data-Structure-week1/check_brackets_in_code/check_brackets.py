# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    Balance = False; 
    nbr_letter = 0 ;
    pos_stack = [] ;
    strings = ['(','[','{',')',']','}'] ;

    for i, next in enumerate(text):
        if next not in strings:
            nbr_letter +=1
            continue

        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pos_stack.append(i+1)
            continue

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                print(i+1)
                quit()

            top = opening_brackets_stack.pop()
            if next == ')': 
                test = Bracket(top,i) 
                Balance = test.Match(')') 

            if next == ']': 
                test = Bracket(top,i) 
                Balance = test.Match(']') 

            if next == '}': 
                test = Bracket(top,i) 
                Balance = test.Match('}') 

        #    print(Balance)

            if  Balance: 
                pos_stack.pop()
            if not Balance: 
                print(i + 1)
                quit()


    if len(opening_brackets_stack) > 0:
        print(pos_stack[-1])
    else:
        print('Success')
