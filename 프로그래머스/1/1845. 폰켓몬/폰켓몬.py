def solution(nums):
    count = len(nums) / 2
    pokemons = set(nums)
    return min(len(pokemons), count)