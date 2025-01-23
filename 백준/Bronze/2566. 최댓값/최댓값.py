row = 0
col = 0
max_value = 0

for i in range(9):
    inputs = list(map(int, input().split()))

    if max_value <= max(inputs):
        max_value = max(inputs)
        row = i + 1
        col = inputs.index(max_value) + 1
    else:
        continue

print(f'{max_value}\n{row} {col}')