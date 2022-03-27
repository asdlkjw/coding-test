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

# from itertools import combinations
# from collections import Counter


# def solution(orders, course):
#     answer = []
#     for c in course:
#         temp = []
#         for order in orders:
#             combi = combinations(sorted(order), c)
#             temp += combi
#         counter = Counter(temp)
#         if len(counter) != 0 and max(counter.values()) != 1:
#             answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

#     return sorted(answer)


# aa = ["AC", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]

# print(Counter(aa))


# 구십구만  829.5 비트

# 12,975,470    10,856.49
# 1,038,000       868.5
# 1,059,600       886.32
# 1,061,316       888
# 1,003,050       839.25
# 1,004,674       840.62
# 7,571,414       6,334.94
# 7,575,037       6,337.95
# 3,523,080       2,947.8
# 3,570,612       2,987.7
# 3,704,580       3,099.6
# 1,474,943       1,234.1
# 1,297,130       1,087.94

# 46,858,906      39,209.21  48,564,527.506

# 619,146     519.3
# 105,636     88.6
# 207,080     138.04
# 753,078     631.62
# 851,300     714

# -752,040        -630.7

# 1,784,200       1,460.86

# 48,643,106      40,670.07   50,373,948.702

# 500,000     403.68 


# 매수금액(수수료?)
# 49,143,106      41,070.07  = 48,824,099(1188.8) 

# 실제입금
# 49,396,739      41,483.17 =  49,315,192(1188.8)    51,381,054

# 현재계좌

# 49,660,000

for i in range(1, 1 << 5):
    print(i)