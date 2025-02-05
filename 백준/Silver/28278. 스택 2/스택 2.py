import sys
stack = []

def stack_order(order):
    if '1' in order:
        x = order.split()[1]
        stack.append(x)
    
    elif order == '2':
        if not stack:   print(-1)
        else:           print(stack.pop())
    
    elif order == '3':
        print(len(stack))
    
    elif order == '4':
        if not stack:   print(1)
        else:           print(0)
    
    elif order == '5':
        if not stack:   print(-1)
        else:           print(stack[-1])

n = int(sys.stdin.readline().strip())

for _ in range(n):
    order = sys.stdin.readline().strip()
    stack_order(order)