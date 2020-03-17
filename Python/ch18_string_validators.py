"""
Challenge:         string validators
Link to Challenge: https://www.hackerrank.com/challenges/string-validators/problem

Author:            Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    str = input()
    print(any(c.isalnum()  for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))
