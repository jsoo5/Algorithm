def solution(dots):
    
    from itertools import combinations
    
    for a, b in combinations(combinations(dots, 2), 2):
        if not ((a[0] in b) or (a[1] in b)):

            x1, y1 = a[0]
            x2, y2 = a[1]
            x3, y3 = b[0]
            x4, y4 = b[1]

            if ((y2 - y1) / (x2 - x1)) == ((y4 - y3) / (x4 - x3)):
                return 1
    return 0