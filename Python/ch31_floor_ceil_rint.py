"""
Challenge:         floor ceil and rint
Link to Challenge: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

Author:            Kaustubh M. Harapanahalli
"""

import numpy as np

my_array = list(map(float, input().split()))
print(str(np.floor(my_array)).replace(
    ".", ". ").replace("[", "[ ").replace(". ]", ".]"))
print(str(np.ceil(my_array)).replace(
    ".", ". ").replace("[", "[ ").replace(". ]", ".]"))
print(str(np.rint(my_array)).replace(
    ".", ". ").replace("[", "[ ").replace(". ]", ".]"))
