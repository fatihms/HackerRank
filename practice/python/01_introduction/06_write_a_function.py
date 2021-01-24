# Write a function
# https://www.hackerrank.com/challenges/write-a-function/problem

# Task

'''
 Given a year, determine whether it is a leap year. 
 If it is a leap year, return the Boolean True, otherwise return False.

 Note that the code stub provided reads from STDIN and passes arguments 
 to the is_leap function. It is only necessary to complete the is_leap function.
'''

# Example

'''
 Sample input: 1990
 Sample output: False
 Explanation: 1990 is not a multiple of 4 hence it's not a leap year.
'''

# Solution

def is_leap(year):
    leap = False
    
    if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        leap = True
   
    return leap

year = int(input())
print(is_leap(year))