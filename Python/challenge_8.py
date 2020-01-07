"""
Challenge: Find the Runner-up Score!

Author:    Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    arr.sort()
    print(arr[-2])
