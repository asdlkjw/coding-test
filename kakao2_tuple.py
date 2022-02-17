def solution(s):
    answer = []
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    count = []
    for i in s:
        i = ''.join(i.split(','))
        count.append(len(i))
    for k in s:
        for i,j in enumerate(count):
            if j == min(count):
                answer.append(s[i])
                count[i] = max(count)+1  
    answer = answer[:len(count)]
    tmp = []
    for i in answer:
        i = i.split(',')
        for tp in i:
            if (int(tp) in tmp) == False:
                tmp.append(int(tp))
    return tmp

####################################################################
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter