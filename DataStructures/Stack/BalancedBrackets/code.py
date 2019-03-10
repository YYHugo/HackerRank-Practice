# https://www.hackerrank.com/challenges/balanced-brackets/problem
# Balanced brackets
#!/bin/python

import math
import os
import random
import re
import sys

class Stack:
    # Constructor
    def __init__(self):
        self.data = []
    # Push (add) new element
    def push(self,n):
        self.data.append(n)
    # Pop element method
    def pop(self):
        return self.data.pop()
    # Pop next element
    def next(self):
        if len(self.data)>0:
            return self.pop()

# Complete the isBalanced function below.
def isBalanced(s):
    stack = Stack()
    pos = 0

    # split in half
    while pos < len(s)/2:
        stack.push(stack, s[pos])
        pos += 1

    pos = len(s)/2
    while pos:
        if(s[pos] != stack.next()):
            break
        if (pos == 0):
            return("YES")

    return("NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

