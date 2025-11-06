def solution(n, lost, reserve):
    losts = set(lost) - set(reserve)
    reserves = set(reserve) - set(lost)
    
    for i in reserves:
        if i - 1 in losts:
            losts.remove(i - 1)
        elif i + 1 in losts:
            losts.remove(i + 1)
            
    return n - len(losts)