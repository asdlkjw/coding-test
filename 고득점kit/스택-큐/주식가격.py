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