"""
Challenge:         zipped!
Link to Challenge: https://www.hackerrank.com/challenges/zipped/problem

Author:            Kaustubh M. Harapanahalli
"""

a = list(map(int, input().split()))

b = []

for i in range(a[1]):
    b.append(list(map(float, input().split())))

for i in zip(*b):
    print("%.1f" % (sum(i)/len(i)))
