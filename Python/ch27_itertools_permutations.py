"""
Challenge:         collections counter
Link to Challenge: https://www.hackerrank.com/challenges/itertools-permutations/problem

Author:            Kaustubh M. Harapanahalli
"""


from itertools import permutations

string, num = input().split()

outputs = list(permutations(string, int(num)))
outputs.sort()

for output in outputs:
    print(''.join(output))