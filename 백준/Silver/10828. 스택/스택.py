import sys

stack = []

def order_function(order):
    if 'push' in order:
        order, x = order.split()
        stack.append(x)

    elif order == 'pop':
        if not stack:   print(-1)
        else:           print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if not stack:   print(1)
        else:           print(0)

    elif order == 'top':
        if not stack:   print(-1)
        else:           print(stack[-1])


n = int(sys.stdin.readline().strip())

for _ in range(n):
    order = sys.stdin.readline().strip()
    order_function(order)
