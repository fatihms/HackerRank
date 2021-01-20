# Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem

# Task

'''
 Given an integer, n, perform the following conditional actions:

 If n is odd, print Weird
 If n is even and in the inclusive range of 2 to 5, print Not Weird
 If n is even and in the inclusive range of 6 to 20, print Weird
 If n is even and greater than 20, print Not Weird
'''

# Example

'''
 Sample input: 3
 Sample output: Weird
 Explanation: n is odd and odd numbers are weird, so print Weird.
'''

# Solution

n = int(input())

if (n % 2 == 1 or (n >= 6 and n <= 20)):
    print('Weird')
else:
    print('Not Weird')