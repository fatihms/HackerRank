# Print Function
# https://www.hackerrank.com/challenges/python-print/problem

# Task

'''
 The included code stub will read an integer, n, from STDIN.
 Without using any string methods, try to print the following:
 123...n
 Note that ... represents the consecutive values in between.
'''

# Example

'''
 Sample input: 3
 Sample output: 123
 Explanation: Printing the list of integers from 1 through 4 as a string, without spaces.
'''

# Solution

n = int(input())
    
for i in range(1, n+1):
    print (i, end="")