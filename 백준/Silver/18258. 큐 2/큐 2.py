import sys
from collections import deque

q = deque()
input = sys.stdin.readline

def process_order(m):
    if 'push' in m:
        x = m.split()[1]
        q.append(x)
    elif m == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif m == 'size':
        print(len(q))
    elif m == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif m == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif m == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])

N = int(input())
for _ in range(N):
    process_order(input().strip())