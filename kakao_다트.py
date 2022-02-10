def solution(dartResult):
    answer = 0
    
    sdt = {
        'S':1,
        'D':2,
        'T':3
    }
    answer = []
    for j,i in enumerate(dartResult):
        if dartResult.find('10') == j:
            i = 10
        elif '0' == i:
            try:
                if '1' == dartResult[j-1]:
                    continue
            except:
                pass
        try:
            tmp = int(i)
        except:
            if '#' == i:
                answer[-1] = -answer[-1]
            elif '*' == i:
                answer[-1] = answer[-1]*2
                try:
                    answer[-2] = answer[-2]*2
                except:
                    pass
            else:
                answer.append(tmp**sdt[i])
        
    
    print(answer)    
    return sum(answer)