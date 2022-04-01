from collections import Counter
from itertools import combinations
from functools import reduce
def multiply(arr):
    return reduce(lambda x, y: x * y, arr)
def solution(clothes):
    answer = 0
    clt = (i[1] for i in clothes)
    clt = (dict(Counter(clt)))
    clt_val = clt.values()
    tmp = len(clt_val)+1
    if tmp == 31:
        return 1073741823
    for i in range(1,tmp):
        cb = combinations(clt_val, i)
        for j in cb:
            answer += multiply(j)
    return answer

# 전체 종류에 콤비네이션 1부터 종류개수까지 늘려감
# 3C2 - 2C2  (총 개수 C 종류 개수) - (각 종류 수 C 종류 개수)

# 222    6 12 8   : 6C1 6C2-3 6C3-12

# 2332   10 37 60 36