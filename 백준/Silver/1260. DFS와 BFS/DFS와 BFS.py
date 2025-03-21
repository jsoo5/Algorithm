import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

def dfs(node):
    visited_d[node] = True
    print(node, end=' ')

    for i in sorted(graph[node]):
        if not visited_d[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_b[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in sorted(graph[node]):
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True

dfs(v)
print()
bfs(v)