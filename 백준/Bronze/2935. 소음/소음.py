import sys
input = sys.stdin.readline

a = int(input())
func = input()
b = int(input())

if '+' in func:
    print(a + b)
else:
    print(a * b)