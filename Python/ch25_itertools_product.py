"""
Challenge: itertools product

Author:    Kaustubh M. Harapanahalli
"""

from itertools import product

a = map(int, input().split())
b = map(int, input().split())

a_b = [a, b]
for i in list(product(*a_b)):
    print(i, end=" ")
