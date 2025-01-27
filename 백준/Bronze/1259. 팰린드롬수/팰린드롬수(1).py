while True:
    num = input()
    if int(num) == 0:
        break

    rev_num = list(reversed(num))
    rev_num = ''.join(rev_num)

    if num == rev_num:
        print('yes')
    else:
        print('no')
