"""
Challenge:         python lists
Link to Challenge: https://www.hackerrank.com/challenges/python-lists/problem

Author:            Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    # N = int(input())
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)