def solution(orders, course):
    from itertools import combinations
    answer = []
    ap = []
    for i in orders:
        for j in i:
            ap.append(j)
    ap = sorted(list(set(ap)))
    
    for cour in course:
        comb = list(combinations(ap, cour))
    
        t1 = [0]*len(comb)

        for order in orders:
            for co,com in enumerate(comb):
                tmp = 0
                for i in com:
                    if i in order:
                        tmp +=1
                if tmp == cour:
                    t1[co] += 1

        t_max = max(t1)
        if t_max >= 2:
            t_mlist = [i for i,j in enumerate(t1) if j == t_max]

            for t_m in t_mlist:
                result = comb[t_m]
                result = ''.join(result)
                answer.append(result)

    return sorted(answer)