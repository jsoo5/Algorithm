import sys

vps = '()'

def judge_vps(string):
    
    if vps in string:
        string = string.replace(vps, '')

        return judge_vps(string)
    
    if not string:
        return 'YES'
    else:
        return 'NO'

T = int(sys.stdin.readline().strip())

for _ in range(T):
    string = sys.stdin.readline().strip()
    
    if string[0] == ')' or string[-1] == '(':
        print('NO')
    else:
        print(judge_vps(string))