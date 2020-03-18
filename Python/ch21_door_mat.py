"""
Challenge:         designer door mat
Link to Challenge: https://www.hackerrank.com/challenges/designer-door-mat/problem

Author:            Kaustubh M. Harapanahalli
"""

n, m = map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
