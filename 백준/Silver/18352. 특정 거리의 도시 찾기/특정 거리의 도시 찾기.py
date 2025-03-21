import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
# print(graph)

distance = [-1] * (n + 1)
result = []

def bfs(start):
    queue = deque([start])
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[node] + 1
            
                if distance[i] == k:
                    result.append(i)
    return result

answer = bfs(x)

if not answer:
    print(-1)
else:
    print('\n'.join(map(str, sorted(answer))))