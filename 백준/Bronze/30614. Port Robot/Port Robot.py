import sys
input = sys.stdin.readline

def check_robot(logs):
    simulation = []

    for log in logs:
        if log.islower():
            simulation.append(log)
        else:
            if simulation and log.lower() == simulation[-1]:
                simulation.pop()
            else :
                return False
            
    if not simulation:
        return True
    else:
        return False
                
n = int(input().strip())
logs = input().strip()

if not logs or logs[0].isupper():
    print(0)
else:
    print(int(check_robot(logs)))