N, M = map(int, input().split())

result = [[0] * M] * N
a = []
b = []

for i in range(N * 2):
    inputs = list(map(int, input().split()))
    
    if i < N:
        a.append(inputs)
    else:
        b.append(inputs)

for n in range(N):
    for m in range(M):
        result[n][m] = a[n][m] + b[n][m]
    print(*result[n])