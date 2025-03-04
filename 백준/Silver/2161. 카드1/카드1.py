import sys
input = sys.stdin.readline

N = int(input())
cards = list(range(1, N+1))
threw = []

while len(cards) != 1:
    first = cards.pop(0)
    threw.append(first)

    new_first = cards.pop(0)
    cards.append(new_first)

print(*threw, *cards, sep=' ')