import sys
input = sys.stdin.readline

n, d = map(int, input().split())
short_way = []

for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= d:
        short_way.append((start, end, length))

dp = [10001] * (d + 1)
dp[0] = 0

for i in range(d + 1):
    if i + 1 <= d:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    
    for start, end ,length in short_way:
        if i == start:
            dp[end] = min(dp[end], dp[start] + length)
print(dp[d])