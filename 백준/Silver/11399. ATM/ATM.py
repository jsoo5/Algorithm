import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

time = []
for i in range(n):
    if not time:
        time.append(p[i])
    else:
        time.append(p[i] + time[i - 1])
print(sum(time))