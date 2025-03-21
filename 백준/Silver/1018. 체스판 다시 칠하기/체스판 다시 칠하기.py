import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input().strip())
# print(board)
cnt1 = []
cnt2 = []

checker1 = ['WBWBWBWB', 'BWBWBWBW']
checker2 = ['BWBWBWBW', 'WBWBWBWB']


def check_color(row, col, checker):
    result = 0
    for i in range(8):
        for j in range(8):
            if board[row + i][col + j] != checker[i % 2][j]:
                result += 1
            else:
                continue
    return result

for p in range(n - 7):
    for q in range(m - 7):
        cnt1.append(check_color(p, q, checker1))
        cnt2.append(check_color(p, q, checker2))
print(min(cnt1 + cnt2))