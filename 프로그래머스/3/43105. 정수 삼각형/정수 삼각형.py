def solution(triangle):
    d = [[0] * (i + 1) for i in range(len(triangle))]
    d[0][0] = triangle[0][0]
    
    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            d[i + 1][j] = max(d[i + 1][j], triangle[i + 1][j] + d[i][j])
            d[i + 1][j + 1] = max(d[i + 1][j + 1], triangle[i + 1][j + 1] + d[i][j])
            
    return max(d[-1])