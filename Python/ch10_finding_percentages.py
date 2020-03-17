"""
Challenge:         finding percentages
Link to Challenge: https://www.hackerrank.com/challenges/finding-the-percentage/problem

Author:            Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x =student_marks[query_name]
    avg = 0
    for i in x:
        avg += i
    avg = avg / len(x)
    print('%.2f' %avg)
