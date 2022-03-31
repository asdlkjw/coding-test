def solution(clothes):
    from collections import Counter
    from itertools import combinations
    answer = 0
    clt = [i[1] for i in clothes]
    
    clt = (dict(Counter(clt)))
    
    print(list(combinations(list(clt.keys()), 2)))
    
    return answer

# 전체 종류에 콤비네이션 1부터 종류개수까지 늘려감
# 3C2 - 2C2  (총 개수 C 종류 개수) - (각 종류 수 C 종류 개수)

# 222    6 12 8   : 6C1 6C2-3 6C3-12

# 2332   10 37 60 36