def solution(relation):
    from itertools import combinations

    answer = []
    answer2= []
    rel = len(relation)
    att = len(relation[0])
    
    tmp = [[] for _ in range(att)]
    test = []
    for i in range(att):
        for j in relation:
            tmp[i].append(j[i])
            
        if len(list(set(tmp[i]))) == rel:
            answer.append(i)
        else:
            test.append(i)
        
    for i in range(2, len(test)+1):
        for j in (list(combinations(test, i))):
            temp = [[] for _ in range(rel)]
            for k in j:
                for z,p in enumerate(tmp[k]):
                    temp[z].append(p)
            if len(list(set([''.join(temp[q]) for q in range(len(temp))]))) == rel:
                answer2.append(j)
    
    for i in answer2:
        if len(i) == min([len(i) for i in answer2]):
            answer.append(i)
    return len(answer)