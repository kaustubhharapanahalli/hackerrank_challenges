"""
Challenge:         introduction to sets
Link to Challenge: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

Author:            Kaustubh M. Harapanahalli
"""


def average(array):
    total = sum(set(array))
    elements = len(set(array))
    return total/elements


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
