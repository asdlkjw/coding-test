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


    import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 내가 생각하는 베스트  코드 
def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)