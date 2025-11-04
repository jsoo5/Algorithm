def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        splited = array[i-1:j]
        splited.sort()
        answer.append(splited[k-1])
    return answer