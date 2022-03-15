def solution(s):
    answer = 0
    import re
    from collections import Counter
    a = {4}
    b = (re.findall(fr'[a-z]{a}',s))  
    print(b)
    print(Counter(b))
    
    return answer