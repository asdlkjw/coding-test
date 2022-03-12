#1번 그리드문제 개쉬움

def solution(money, costs):
    answer = []
    won = [1,5,10,50,100,500]

    grid = [won[i] / costs[i] for i in range(len(costs))]

    for _ in (costs):
        g_m_list = []
        g_m = max(grid)

        for i,j in enumerate(grid):
            if j == g_m:
                g_m_list.append(i)
        grid[g_m_list[-1]] = 0
        answer.append(costs[g_m_list[-1]]*(money//won[g_m_list[-1]]))
        money = money - (won[g_m_list[-1]]*(money//won[g_m_list[-1]]))

        del g_m_list[-1]

    return sum(answer)


#2번 정사각형에서 안으로 회전하며 들어감  이상하게 안풀리네;; 쉬운거 같은디..
def solution(n, clockwise):
    import math 

    answer = [[0]*n for _ in range(n)] 
    m = n/2
    if n%2 != 0:
        m = math.ceil(n/2)


    wide = []
    for i in range(n, 1, -2):
        if i != 1:
            wide.append(i-1)
    if n%2 != 0:
        wide.append(1)

    print(wide)

    for turn in range(4):
        pass
    if clockwise != False:
        stack = []
        for q,wid in enumerate(wide):
            q = q+1
            if q%4 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[li-(i+1)][up] = price+j           
            elif q%3 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[li][stack[-1]-1-(i+1)] = price+j
                up = stack[-1]-wid
                price = price + wid
            elif q%2 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[i+1][stack[-1]-1] = stack[-1]+j
                li = wid+1
                price = stack[-1]+wid
            elif q%1 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[0][i] = j

                stack.append(answer[0][wid-1])


            print(stack)

    else:
        stack = []
        for q,wid in enumerate(wide):
            q = q+1
            if q%4 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[li-(i+1)][up-1] = price+j  
                li = li-wid
                up = up-1 
                price = price + wid
            elif q%3 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[li][stack[-1]-1-(i+1)] = price+j
                up = stack[-1]-wid
                price = price + wid
            elif q%2 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[i+1][stack[-1]-1] = stack[-1]+j
                li = wid+1
                price = stack[-1]+wid
            elif q == 1:
                for i,j in enumerate(range(1,wid+1)):
                    answer[0][i] = j

                stack.append(answer[0][wid-1])
            elif q%1 == 0:
                for i,j in enumerate(range(1,wid+1)):
                    answer[li][up+i] = price +j

                up = up+wid
                price = price+wid
            print(stack)

        # for i in range(wid+1):
        #     answer[i][wide[0]] = 




    # for i,j in enumerate(range(1, n)):
    #     answer[i][n-1] = j

    return answer

# 3번 문제 최소거리 구하는 문제 ;; 까비
def solution(width, height, diagonals):
    import math
    answer = 0

    answer = (math.factorial(width+height) / (math.factorial(width)*math.factorial(height)))
    answer = answer * len(diagonals)

    a = ((math.factorial(17+19) / (math.factorial(17)*math.factorial(19))))
    b = (math.factorial(51-17+2 + 37-19 )/(math.factorial(51-17+1)*math.factorial(37-19+1)))


    print((b/2)*a)
    # print(a*b)
    return answer%10000019