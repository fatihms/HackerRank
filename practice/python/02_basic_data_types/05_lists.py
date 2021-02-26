# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

# Task

'''
  Consider a list (list = []). You can perform the following commands:

  1.insert i e: Insert integer e at position i.
  2.print: Print the list.
  3.remove e: Delete the first occurrence of integer e.
  4.append e: Insert integer e at the end of the list.
  5.sort: Sort the list.
  6.pop: Pop the last element from the list.
  7.reverse: Reverse the list.
  Initialize your list and read in the value of n followed by n
  lines of commands where each command will be of the 7 types listed above. 
  Iterate through each command in order and perform the corresponding operation on your list.
'''

# Example

'''
 Sample input: 
  12
  insert 0 5
  insert 1 10
  insert 0 6
  print
  remove 6
  append 9
  append 1
  sort
  print
  pop
  reverse
  print
 Sample output: 
  [6, 5, 10]
  [1, 5, 9, 10]
  [9, 5, 1]
 Explanation: 
'''

# Solution

if __name__ == '__main__':
    N = int(input())
    
    l = []
    for i in range(N):
        target = input().split()
        
        if (target[0] == 'insert'):
            l.insert(int(target[1]), int(target[2]))
        elif (target[0] == 'print'):
            print(l)
        elif (target[0] == 'remove'):
            l.remove(int(target[1]))
        elif (target[0] == 'append'):
            l.append(int(target[1]))
        elif (target[0] == 'sort'):
            l.sort()
        elif (target[0] == 'pop'):
            l.pop()
        elif (target[0] == 'reverse'):
            l.reverse()

