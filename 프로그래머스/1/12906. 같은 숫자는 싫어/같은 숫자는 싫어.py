
def solution(arr):
    answer = []
    for i in arr:
        answer.append(i)
        if len(answer) < 2:
            continue
        if answer[-1] == answer[-2]:
            answer.pop()
            
    return answer