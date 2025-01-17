while True:
    a, b = map(int, input().split(' '))

    if a == 0 and b == 0:
        break
        
    elif b % a == 0:
        print('factor')
        continue
        
    elif a % b == 0:
        print('multiple')
        continue
        
    else:
        print('neither')
        continue