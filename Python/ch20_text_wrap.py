"""
Challenge:         text wrap
Link to Challenge: https://www.hackerrank.com/challenges/text-wrap/problem

Author:            Kaustubh M. Harapanahalli
"""

import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.TextWrapper(width=max_width).wrap(text=string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
