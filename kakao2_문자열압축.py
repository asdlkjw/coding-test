def solution(s):
    # from collections import Counter
    # print(Counter(s))
    answer = 0
    import re
    for i in range(1,len(s)+1):
        a = f'{s[:i]}'
        print(re.split(rf'{(a)}+', s))
        print(a)
    
    s[0][:2]    
    return answer