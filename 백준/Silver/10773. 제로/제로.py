k = int(input())
num_list = []

for _ in range(k):
    called_num = int(input())
    if called_num != 0:
        num_list.append(called_num)
    else:
        num_list.pop()

if len(num_list) == 0:  print(0)
else:                   print(sum(num_list))