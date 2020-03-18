"""
Challenge:         swap case
Link to Challenge: https://www.hackerrank.com/challenges/swap-case/problem

Author:            Kaustubh M. Harapanahalli
"""


def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
