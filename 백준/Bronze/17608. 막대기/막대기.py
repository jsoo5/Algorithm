import sys

N = int(sys.stdin.readline().strip())
sticks = []
shown_cnt = 0

for _ in range(N):
    sticks.append(int(sys.stdin.readline().strip()))

highest = sticks[-1]

for i in range(N-1, -1, -1): # index 5~0
    if sticks[i] > highest:
        shown_cnt += 1
        highest = sticks[i]
    else:
        continue
print(shown_cnt + 1)