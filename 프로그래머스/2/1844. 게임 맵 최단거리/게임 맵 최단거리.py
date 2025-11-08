from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    def bfs(y, x):
        queue = deque()
        queue.append((y, x))
        
        while queue:
            y, x = queue.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if maps[ny][nx] == 0:
                    continue
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((ny, nx))
        return maps[n - 1][m - 1]

    if bfs(0, 0) == 1:
        return -1
    else:
        return bfs(0, 0)