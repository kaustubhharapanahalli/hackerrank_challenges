"""
Challenge:         python tuples
Link to Challenge: https://www.hackerrank.com/challenges/python-tuples/problem

Author:            Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = tuple(integer_list)
    print(hash(my_tuple))
