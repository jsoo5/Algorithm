import string

n, b = input().split(' ')
b = int(b)

alphbet = [i for i in string.ascii_uppercase]
value = 10
alpha_dict = {}

for alpha in alphbet:
    alpha_dict[alpha] = value
    value += 1
    
result = 0
for i in range(len(n)):
    idx = len(n) - i - 1
    if n[idx] in alpha_dict:
        result += alpha_dict.get(n[idx]) * (b**i)
    else:
        result += int(n[idx]) * (b**i)
print(result)