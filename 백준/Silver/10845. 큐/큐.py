import sys
input = sys.stdin.readline

def check_order(q, order):
    if 'push' in order:
        num = order.split()[1]
        q.append(num)
    elif order == 'pop':
        if q:
            print(queue[0])
            del q[0]
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)

N = int(input())
queue = []
for _ in range(N):
    inputs = input().strip()
    check_order(queue, inputs)

