# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Task

'''
 Given the participants' score sheet for your University Sports Day, 
 you are required to find the runner-up score. You are given n scores. 
 Store them in a list and find the score of the runner-up.
'''

# Example

'''
 Sample input: 
  5
  2 3 6 6 5
 Sample output: 5
 Explanation: Given list is [2 3 6 6 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

# Solution

n = int(input())
arr = map(int, input().split())
    
my_list = list(arr)
my_list.sort()

i = 0
while(len(my_list)):
    if(my_list[-1] != my_list[-1-i]):
        print(my_list[-1-i])
        break
    i = i + 1