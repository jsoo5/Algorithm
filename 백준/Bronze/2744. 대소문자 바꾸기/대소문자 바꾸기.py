import sys

word = sys.stdin.readline().strip()
changed = []

for n in word:
    if n.isupper():
        changed.append(n.lower())
    else:
        changed.append(n.upper())
print(*changed, sep='')