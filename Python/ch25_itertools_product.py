"""
Challenge:         collections counter
Link to Challenge: https://www.hackerrank.com/challenges/collections-counter/problem

Author:            Kaustubh M. Harapanahalli
"""

from itertools import product

a = map(int, input().split())
b = map(int, input().split())

a_b = [a, b]
for i in list(product(*a_b)):
    print(i, end=" ")
