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


def solution(relations):
    answer = []
    targets = [[i for i in range(len(relations[0]))]]
    while targets:
        check = 0
        tmp = targets.pop(0)
        for i in range(len(tmp)):
            lst = []
            for leng in range(len(relations)):
                a = tmp.copy()
                a.remove(tmp[i])
                b = ''
                for x in a:
                    b += relations[leng][x]
                lst.append(b)
            if (len(set(lst)) == len(lst)) and (a not in targets):
                targets.append(a)
            elif (len(set(lst)) != len(lst)):
                check +=1
        if check ==len(tmp):
            answer.append(tmp)
    return len(answer)




def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)