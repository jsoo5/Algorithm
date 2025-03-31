import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = int(y * 100 / x)

start = 1
end = 10**9

def binary_search(target, start, end):

    while start <= end:
        mid = (start + end) // 2
        win_per = int((y + mid) / (x + mid) * 100)

        if win_per > target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer
    
if z >= 99:
    print(-1)
else:
    print(binary_search(z, start, end))