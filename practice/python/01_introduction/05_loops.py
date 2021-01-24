# Loops
# https://www.hackerrank.com/challenges/python-loops/problem

# Task

'''
 The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2.
'''

# Example

'''
 Sample input: 5
 Sample output: 
    0
    1
    4
    9
    16
 Explanation: 
    The list of non-negative integers that are less than n = 5 is [0, 1, 2, 3, 4]. Print the square of each number on a separate line.
'''

# Solution

n = int(input())

for i in range(n):
    print(i ** 2)