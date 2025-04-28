import sys
input = sys.stdin.readline

N, L, K = map(int, input().split())
cnt = [0] * 2
result = 0

for _ in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        cnt[1] += 1
    elif sub1 > L and sub2 > L:
        continue
    else:
        cnt[0] += 1

rest = K - cnt[1]
result += min(K, cnt[1]) * 140
if rest > 0:
    result += min(rest, cnt[0]) * 100
print(result)