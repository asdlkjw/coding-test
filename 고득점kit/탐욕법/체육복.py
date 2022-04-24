def solution(n, lost, reserve):
    answer = n - len(lost)
    tmp = []
    for i in (reserve):
        tmp.append(i-1)
        tmp.append(i+1)
        
    for i in lost:
        if (tmp.count(i)) > 0:
            answer += 1
    
    return answer