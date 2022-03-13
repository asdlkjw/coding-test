# def gen_combinations(arr, n):
#     result =[] 
#     if n == 0:
#         # print(arr, f'@@@@@@')
#         return [[]]
#     for i in range(0, len(arr)):
#         elem = arr[i] 
#         rest_arr = arr[i + 1:]
#         # print(elem, rest_arr, ' elem, rest_arr', i)
#         for C in gen_combinations(rest_arr, n-1):
#             result.append([elem]+C) 
#             # print('append ')
            
#     print(arr, f'@@@@@@', '끝')
    
#     return result


# print(gen_combinations([2,4,5,2,5], 3))

# # def aaa(n):
# #     print(f'불렀나 {n}')
# #     if n == 0:
# #         return print(f'종료')
# #     aaa(n-1)
    
# #     print((f'재귀 인가?{n}'))
# #     return print(f'재귀 들어간다{n}')

# aaa(10)

# import re

# key = 'asldkjfaefaefdsf'

# if 'af'in key:
#     print('dd')
    
# print(re.findall(r'[a|f|s]', key))

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


aa = ["AC", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]

print(Counter(aa))
