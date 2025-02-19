import sys
n_1, k_1, n_2, k_2 = sys.stdin.readline().split()

business = int(n_1) * int(k_1)
economy = int(n_2) * int(k_2)
print(business + economy)
