numbers = [0] * 9

for i in range(9):
    numbers[i] = int(input())

max_value = max(numbers)

print(max_value)
print(numbers.index(max_value) + 1)