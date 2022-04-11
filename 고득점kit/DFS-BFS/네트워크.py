def solution(progresses, speeds):
    answer = []
    import math
    pro = [100-i for i in progresses]
    speed = ([math.ceil(i/j) for i,j in zip(pro, speeds)])
    print(speed)
    
    
    return answer