# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem

# Task

'''
  Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
'''

# Example

'''
 Sample input: 
  2
  1 2
 Sample output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
 Explanation: 3713081631934410656
'''

# Solution

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))

