def solution(prices):
    answer  = [0]*len(prices)
    for i in range(len(prices)):
        for price in prices[i+1:]:
            if prices[i] <= price:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        time = len(prices) - i -1
        for i_p in range(i+1,len(prices)):
            if prices[i_p] < prices[i]:
                time = i_p - i
                break
        answer.append(time)
    answer.append(0)
    return answer