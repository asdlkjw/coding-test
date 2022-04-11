def solution(progresses, speeds):
    answer = []
    import math
    pro = [100-i for i in progresses]
    speed = ([math.ceil(i/j) for i,j in zip(pro, speeds)])
    speed.append(101)
    tmp = []
    for i,j in enumerate(speed):
        if i == 0 :
            tmp.append(j)
            continue
        if tmp[0] >= j:
            tmp.append(j)
        elif tmp[0] < j:
            answer.append(len(tmp))
            tmp = []
            tmp.append(j)
    return answer