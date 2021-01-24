# Arithmetic Operators
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

# Task

'''
 The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

 The first line contains the sum of the two numbers.
 The second line contains the difference of the two numbers (first - second).
 The third line contains the product of the two numbers.
'''

# Example

'''
 Sample input:
    3
    2
 Sample output:
    5
    1
    6
 Explanation:
    3 + 2 => 5
    3 - 2 => 1
    3 * 2 => 6
'''

# Solution

a = int(input())
b = int(input())
    
print((a + b), (a - b), (a * b), sep='\n')