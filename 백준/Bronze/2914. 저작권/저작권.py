import sys
input = sys.stdin.readline

a, i = map(int, input().split())
melody = a * (i - 1) + 1
print(melody)