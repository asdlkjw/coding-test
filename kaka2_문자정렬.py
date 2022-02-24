import re
def quick_sort(array):

    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if int(re.sub(r'[^0-9]', '', x)) < int(re.sub(r'[^0-9]', '', pivot))]
    right_side = [x for x in tail if int(re.sub(r'[^0-9]', '', x)) >= int(re.sub(r'[^0-9]', '', pivot))]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def solution(files):
    
    files3 = [x.split('.')[0] for x in files]
    top = sorted(list(set([ x[:1].lower() for x in files ])))
    
    answer = []
    if len(top) > 1:
        files2 = sorted(word.lower() for word in files3)
        top = sorted(list(set([x[:1] for x in files2])))
    else:
        files2 = [word.lower() for word in files3]
        
    
    files2 += '_'
    best = []
    for i in top:
        tmp = 0
        check = False
        for j,k in enumerate(files2):
            if k[0] == i:
                if check != True:
                    tmp = j
                check = True
                pass
            elif check != False:
                best.append(files2[tmp:j])
                break
    
    for i in range(len(best)):
        
        answer += quick_sort(best[i])
    
    for i in files:
        j = i.split('.')[0]
        answer[answer.index(j.lower())] = i

    print(answer)
    return answer

############################################

import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]


import re

def solution(files):
    a = sorted(files, key=lambda file : int( re.findall('\d+', file)[0] ))

    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b