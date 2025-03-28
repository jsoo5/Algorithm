scores = {'A+':4.5, 'A0': 4.0, 'B+':3.5, 'B0':3.0, 
          'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
sub_sum = 0
total_credit = 0

for i in range(20):
    _, credit, grade = input().split()
    credit = float(credit)

    if grade != 'P':
        sub_sum += credit * scores.get(grade)
        total_credit += credit
    else:
        continue

result = sub_sum / total_credit
print(f'{result:.6f}')