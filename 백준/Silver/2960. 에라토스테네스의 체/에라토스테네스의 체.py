n, k = map(int, input().split())
deleted = []

while len(deleted) <= n-2:

    for p in range(2, n+1):
        if p in deleted:
            continue

        for del_p in range(p, n+1, p):
            if not del_p in deleted:
                deleted.append(del_p)
print(deleted[k-1])