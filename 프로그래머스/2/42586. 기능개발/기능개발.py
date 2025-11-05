import math

def solution(progresses, speeds):
    deploys = []
    prev_day = 0
    
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        
        if prev_day < day:
            deploys.append(1)
        else:
            deploys[-1] += 1
        
        prev_day = max(prev_day, day)            
        
    return deploys