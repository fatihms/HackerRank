# List Comprehensions
# https://www.hackerrank.com/challenges/list-comprehensions/problem

# Task

'''
 Let's learn about list comprehensions! You are given three integers
 x, y and z representing the dimensions of a cuboid along with an integer n.
 Print a list of all possible coordinates given by (i, j, k) on a 3D grid where
 the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 
 Please use list comprehensions rather than multiple loops, as a learning exercise.
'''

# Example

'''
 Sample input: 
  x = 1
  y = 1
  z = 1
  n = 2
 Sample output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
 Explanation: 
  Each variable x,y and z will have values of 0 or 1. All permutations of lists in the form
  [i, j, k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
  Remove all arrays that sum to n = 2 to leave only the valid permutations.
'''

# Solution

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

