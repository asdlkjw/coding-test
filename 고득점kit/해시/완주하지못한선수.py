# 내 풀이 10분컷
def solution(participant, completion):
    from collections import Counter
    for i,j in dict(Counter(participant + completion)).items():
        if j%2 : answer = i
    return answer


# 베스트 풀이   dict 은 사칙연산이 안되지만 Counter 객체는 뺄셈이 가능하다
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]



#정석 풀이

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

