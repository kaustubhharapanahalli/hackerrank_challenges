"""
Challenge:         what's your name
Link to Challenge: https://www.hackerrank.com/challenges/whats-your-name/problem

Author:            Kaustubh M. Harapanahalli
"""


def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
