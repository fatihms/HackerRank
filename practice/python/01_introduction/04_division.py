# Division
# https://www.hackerrank.com/challenges/python-division/problem

# Task

'''
 The provided code stub reads two integers, a and b, from STDIN.

 Add logic to print two lines. The first line should contain the result of integer division,  
 a // b . The second line should contain the result of float division, a / b.

 No rounding or formatting is necessary.
'''

# Example

'''
 Sample input: 
    4
    3
 Sample output: 
    1
    1.33333333
 Explanation: 
    The result of the integer division 4 // 3.
    The result of the float division is 4 / 3.
'''

# Solution

a = int(input())
b = int(input())
    
print(a // b, a / b, sep='\n')