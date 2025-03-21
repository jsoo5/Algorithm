import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
# print(graph)

visited = [False] * (n + 1)
distance = [0] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[node] + 1
bfs(x)

if k in distance:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
else:
    print(-1)