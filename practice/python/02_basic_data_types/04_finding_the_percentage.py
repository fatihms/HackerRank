# Finding the percentage
# https://www.hackerrank.com/challenges/python-lists/problem

# Task

'''
  The provided code stub will read in a dictionary containing key/value pairs of name:
  [marks] for a list of students. Print the average of the marks array for the student 
  name provided, showing 2 places after the decimal.
'''

# Example

'''
 Sample input: 
  3
  Krishna 67 68 69
  Arjun 70 98 63
  Malika 52 56 60
  Malika
 Sample output: 56.00
 Explanation: Marks for Malika are {52, 56, 60} whose average is 56
'''

# Solution

if __name__ == '__main__':
    
    n = int(input())
    
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    
average = sum(student_marks[query_name])/3
print('%.2f' %average)
