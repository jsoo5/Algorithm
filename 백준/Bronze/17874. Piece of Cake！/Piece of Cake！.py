import sys
input = sys.stdin.readline

n, h, v = map(int, input().split())
depth = 4

width = max(n - h, h)
height = max(n - v, v)

print(width * height * depth)