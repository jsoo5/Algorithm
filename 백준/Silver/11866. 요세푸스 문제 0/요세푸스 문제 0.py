import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n_list = list(range(1, N+1))
del_list = []

idx = 0
while n_list:
    idx += K - 1
    idx %= len(n_list)
    deleted = n_list.pop(idx)
    del_list.append(deleted)

print(f'<{", ".join(map(str, del_list))}>')