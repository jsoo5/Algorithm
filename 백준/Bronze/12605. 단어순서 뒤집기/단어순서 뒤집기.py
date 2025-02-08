import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    L = list(sys.stdin.readline().strip().split(' '))
    L = ' '.join(L[::-1])
    
    print(f'Case #{i+1}: {L}')