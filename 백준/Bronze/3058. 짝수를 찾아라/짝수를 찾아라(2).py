T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))

    even = [i for i in numbers if i % 2 == 0]
    print(sum(even), min(even))
