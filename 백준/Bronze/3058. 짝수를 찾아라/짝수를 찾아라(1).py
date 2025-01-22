T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))

    even = []
    sum = 0

    for i in numbers:
        if i % 2 == 0:
            sum += i
            even.append(i)
    
    print(sum, min(even))
