def solution(numbers, target):
    result = 0
    def dfs(num, level):
        nonlocal result

        if level == len(numbers):
            if num == target:
                result += 1
            return

        signs = [-num, num]
        if level == 1:
            for i in range(2):
                dfs(signs[i] + numbers[level], level + 1)
                dfs(signs[i] - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 1)
    return result


##########################dfs 정석

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer