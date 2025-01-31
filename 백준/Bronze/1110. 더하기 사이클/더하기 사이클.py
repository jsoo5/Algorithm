number = input()

if len(number) == 1:
    number = '0' + number

before_num = number
new_num = -1
count = 0

while number != new_num:
    
    num_sum = int(before_num[0]) + int(before_num[1])
    num_sum = str(num_sum)
    new_num = before_num[-1] + num_sum[-1]
    
    before_num = new_num
    count += 1

print(count)