import math

m, n = map(int, input().split())

numbers = [_ for _ in range(m, n+1)]
prime_judge = [True] * len(numbers)
sqrt_num = int(math.sqrt(n))

for mul in range(2, sqrt_num+1):
    for num in range(mul*mul, n+1, mul):
        if num >= m:
            prime_judge[num - m] = False

if numbers[0] == 1:
    prime_judge[0] = False

for idx in range(len(numbers)):
    if prime_judge[idx]:
        print(numbers[idx])