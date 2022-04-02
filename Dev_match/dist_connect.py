dist	result
[[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]	[[1,2,0,4,3],[3,4,0,2,1]]
[[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]	[[0,3,1,2],[2,1,3,0]]

def solution(dist):
    from collections import Counter
    answer = []
    answer_z = []
    temp = []
    for dis in dist:
        tmp = []
        tp = []
        for i,j in enumerate(sorted(dis)):
            tmp.append(dis.index(j))

        if len(set(tmp)) == len(tmp):
            # tp.append(sum(tmp[:tmp.index(0)]))
            # tp.append(sum(tmp[tmp.index(0):]))
            l = sum(tmp[:tmp.index(0)])
            r = sum(tmp[tmp.index(0):])
            temp.append(abs(l-r))
            answer.append(tmp)
    a = Counter(temp)
    for i,j in a.items():
        if j == max(a.values()):
            for z, k in enumerate(temp):
                if k == i:
                    answer_z.append(answer[z])

    return sorted(answer_z)