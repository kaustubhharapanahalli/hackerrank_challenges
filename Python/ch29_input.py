"""
Challenge:         input
Link to Challenge: https://www.hackerrank.com/challenges/input/problem

Author:            Kaustubh M. Harapanahalli
"""

x, b = list(map(int, input().split()))
c = eval(input())

if c == b:
    print("True")
else:
    print("False")
