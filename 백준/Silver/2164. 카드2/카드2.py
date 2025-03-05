import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

N = int(input())
cards = list(range(1, N+1))
queue.extend(cards)

while len(queue) != 1:
    queue.popleft()
    first = queue.popleft()
    queue.append(first)
print(*queue)