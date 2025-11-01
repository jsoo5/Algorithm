def solution(dots):
    
    from itertools import combinations
    comb = []
    
    for i in combinations(combinations(dots, 2), 2):
        if not ((i[0][0] in i[1]) or (i[0][1] in i[1])):
            x1, y1, x2, y2 = i[0][0][0], i[0][0][1], i[0][1][0], i[0][1][1]
            x3, y3, x4, y4 = i[1][0][0], i[1][0][1], i[1][1][0], i[1][1][1]
            print(i)

            if ((y2 - y1) / (x2 - x1)) == ((y4 - y3) / (x4 - x3)):
                return 1
    return 0