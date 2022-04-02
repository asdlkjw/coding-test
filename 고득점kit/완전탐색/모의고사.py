def solution(answers):
    answer = []
    tmp = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    temp = []
    for i in tmp: temp.append(i * (int(len(answers)/len(i))+1))
    for i in temp :
        ans = 0
        for j,k in zip(i, answers):
            if j == k: ans += 1 
        answer.append(ans)
    if answer.count(max(answer)) == 1:
        return [(answer.index(max(answer)) + 1)]
    else:
        answer2 = []
        for i,j in enumerate(answer):
            if j == max(answer): answer2.append(i+1)
        return answer2
    
    
def solution(answers):
    p = [[1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]