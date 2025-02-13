import sys
input = sys.stdin.readline

scores = []
score_sum = 0

for _ in range(5):
    scores.append(int(input().strip()))

for score in scores:
    if score < 40:
        score = 40
    score_sum += score
print(score_sum // 5)