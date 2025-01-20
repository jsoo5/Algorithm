N, M = map(int, input().split())

baskets = [n + 1 for n in range(N)]
changed = baskets[:]

for m in range(M):
    i, j = map(int, input().split())
    
    i -= 1
    j -= 1
    
    for idx in range(abs(i - j) + 1):
        changed[j - idx] = baskets[i + idx]

    baskets = changed[:]

print(*baskets)