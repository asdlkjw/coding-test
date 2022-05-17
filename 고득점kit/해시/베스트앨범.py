def solution(genres, plays):
    answer = []
    name = {}
    for i in set(genres):
        count = []
        for j in range(len(plays)):
            if i == genres[j]:
                count.append(plays[j])
        name[i] = count
        
    q = sorted(name.items(), key = lambda item: sum(item[1]) , reverse = True)
    
    pq = []
    for p in q:
        pq.append(sorted(p[1], reverse=True))
    
    for i in pq:
        for a,k in enumerate(i):
            if a >= 2:
                continue
            for ans,j in enumerate(plays):
                if k == j:
                    answer.append(ans)
                    
    return answer