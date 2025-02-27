import sys
input = sys.stdin.readline

_ = input()
h = list(map(int, input().split()))
a = list(map(int, input().split()))
print(max(h) + max(a))