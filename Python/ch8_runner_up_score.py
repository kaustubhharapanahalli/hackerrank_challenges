"""
Challenge:         runner up score
Link to Challenge: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Author:            Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    arr.sort()
    print(arr[-2])
