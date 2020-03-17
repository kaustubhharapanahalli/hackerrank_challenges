"""
Challenge:         if else
Link to Challenge: https://www.hackerrank.com/challenges/py-if-else/problem

Author:            Kaustubh M. Harapanahalli
"""

N = int(input().strip())

if N % 2 != 0 or (N % 2 == 0 and 6 <= N <= 20):
    print("Weird")
elif (N % 2 == 0 and 2 <= N <= 5) or (N % 2 == 0 and N > 20):\
    print("Not Weird")
