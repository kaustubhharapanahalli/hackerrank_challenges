"""
Challenge: Find a String

Author:    Kaustubh M. Harapanahalli
"""

def count_substring(string, sub_string):
    ind, count, start_flag = 0,0,0
    while True:
        try:
            if start_flag == 0:
                ind = string.index(sub_string)
                start_flag = 1
            else:
                ind += 1 + string[ind+1:].index(sub_string)
            count += 1
        except:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)