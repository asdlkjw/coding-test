def solution(info, query):
    import pandas
    answer = []    
    info = [inf.split() for inf in info]
    query = [quer.replace('and', '').split() for quer in query]
    for i in (query):
        df = pandas.DataFrame(info, columns = ['언어','직군','경력','푸드','점수'])
        df['점수'] = df.점수.astype('int')
        if i[0] != '-':
            df = df[(df['언어'] == f'{i[0]}')]
        if i[1] != '-':
            df = df[(df['직군'] == f'{i[1]}')]
        if i[2] != '-':
            df = df[(df['경력'] == f'{i[2]}')]
        if i[3] != '-':
            df  = df[(df['푸드'] == f'{i[3]}')]
        if i[4] != '-':
            df = df[(df['점수'] >= int(f'{i[4]}'))]
        answer.append(df.shape[0])
    
    return answer

import bisect, itertools, collections

def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers