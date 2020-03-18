"""
Challenge:         default dictionary tutorial
Link to Challenge: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

Author:            Kaustubh M. Harapanahalli
"""

from collections import defaultdict

group_a, group_b = map(int, input().split())
list_1 = []

dict_values = defaultdict(list)
for i in range(group_a):
    key = input()
    dict_values[key].append(i+1)

for i in range(group_b):
    list_1.append(input())

for i in list_1:
    if i in dict_values:
        print(" ".join(map(str, dict_values[i])))
    else:
        print(-1)
