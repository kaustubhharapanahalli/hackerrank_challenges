"""
Challenge: String Split and Join

Author:    Kaustubh M. Harapanahalli
"""

def split_and_join(line):
    line_list = line.split()
    return '-'.join(line_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
