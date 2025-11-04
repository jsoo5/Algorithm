def solution(participant, completion):
    hash = dict()
    
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    
    for c in completion:
        if c in hash:
            hash[c] -= 1
    
    for player, count in hash.items():
        if count > 0:
            return player
        