"""
Challenge:         polar coordinates
Link to Challenge: https://www.hackerrank.com/challenges/polar-coordinates/problem

Author:            Kaustubh M. Harapanahalli
"""

import cmath

input_number = eval(input())
print(abs(input_number))
print(cmath.phase(input_number))
