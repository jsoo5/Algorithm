import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return 1
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
result = []

for i in range(m):
    result.append(binary_search(cards, numbers[i], 0, n - 1))
print(*result, end=' ')