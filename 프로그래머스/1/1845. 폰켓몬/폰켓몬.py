def solution(nums):
    count = len(nums) / 2
    pokemons = dict()
    
    for i in nums:
        if i in pokemons:
            pokemons[i] += 1
        else:
            pokemons[i] = 1
    
    if len(pokemons) < count:
        return len(pokemons)
    else:   
        return count