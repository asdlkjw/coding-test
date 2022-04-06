def solution(brown, yellow):
    answer = []
    result = brown + yellow  
    for i in range(3,result-2):
        x, y = (result/i, i)
        if (x+y)*2 -4 == brown:
            answer.append([int(x), int(y)])
    return answer[0]