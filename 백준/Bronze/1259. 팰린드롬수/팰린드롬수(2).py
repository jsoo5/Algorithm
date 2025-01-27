while True:
    num = input()
    if int(num) == 0:
        break

    if num == num[::-1]:
        print('yes')
    else:
        print('no')
