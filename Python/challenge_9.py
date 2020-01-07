"""
Challenge: Nested Lists

Author:    Kaustubh M. Harapanahalli
"""

if __name__ == '__main__':
    scores = []
    scores2 = []
    details = []
    details2 = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        details.append([name,score])
    min_score = min(scores)
    for stud_name, stud_score in details:
        if stud_score != min_score:
            details2.append([stud_name,stud_score])
            scores2.append(stud_score)
    x = min(scores2)
    for i,val in details2:
        if val == x:
            names.append(i)
    names.sort()
    for name in names:
        print(name)
