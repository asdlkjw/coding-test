
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

# 나의 풀이
def solution(N, stages):
    answer = []
    answer2 = []
    stages2 = range(1,N+1)
    for i in stages2:
        if stages.count(i) != 0:
            answer2.append(stages.count(i)/len([j for j in stages if (j >= i)] ))
        else:
            answer2.append(0)
    for i in answer2:
        x = answer2.index(max(answer2))
        answer.append(x+1)
        answer2[x] = -1

    return answer

    #########################################
# best 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
