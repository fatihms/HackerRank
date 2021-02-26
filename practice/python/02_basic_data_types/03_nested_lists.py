# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

# Task

'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names 
alphabetically and print each name on a new line.
'''

# Example

'''
 Sample input: 
  5
  Harry
  37.21
  Berry
  37.21
  Tina
  37.2
  Akriti
  41
  Harsh
  39
 Sample output: 
  Berry
  Harry
 Explanation: 
  There are 5 students in this class whose names and grades are assembled to build the following list:

  python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

  The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
  so we order their names alphabetically and print each name on a new line.
'''

# Solution

records = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
second_lowest_grade = set([score for name, score in records])
second_lowest_grade = sorted(list(second_lowest_grade))[1]

students = sorted([name for name, score in records if score == second_lowest_grade])

print(*students, sep='\n')


