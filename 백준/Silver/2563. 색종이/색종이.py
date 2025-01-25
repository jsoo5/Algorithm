paper = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for n in range(100):
    cnt += paper[n].count(1)

print(cnt)