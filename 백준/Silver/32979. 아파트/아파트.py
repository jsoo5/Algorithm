import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
loser = []

def game_start(apart, num):
    i = 1
    while i < num:
        apart.append(apart.pop(0))
        i += 1
    return apart[0]

for j in range(T):
    loser.append(game_start(a, b[j]))
print(*loser, sep=' ')
