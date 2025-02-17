import sys
input = sys.stdin.readline

def calc_score(cnt):
    score = 56 * cnt[0] + 24 * cnt[1] + 14 * cnt[2] + 6 * cnt[3]
    return score

counts = list(map(int, input().split()))
print(calc_score(counts))