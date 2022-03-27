def solution(relation):
    from itertools import combinations

    answer = []
    rel = len(relation)
    att = len(relation[0])
    
    tmp = [[] for _ in range(att)]
    
    for i in range(att):
        for j in relation:
            tmp[i].append(j[i])
            
        if len(list(set(tmp[i]))) == rel:
            answer.append(i)
        else:
            print(i)
    
    print(answer)
    return 2