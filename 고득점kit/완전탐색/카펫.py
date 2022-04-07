def solution(brown, yellow):
    answer = []
    result = brown + yellow  
    for i in range(3,result-2):
        x, y = (result/i, i)
        if (x+y)*2 -4 == brown:
            answer.append([int(x), int(y)])
    return answer[0]


##########################################

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
            
            