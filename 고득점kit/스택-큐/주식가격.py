def solution(prices):
    answer  = [0]*len(prices)
    for i in range(len(prices)):
        for price in prices[i+1:]:  # 여기 코드의 차이로 시간초과가 떴음...   n제곱으로 짤때는 리스트를 바로 사용하지 않고 변수에 넣어서 사용하자
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

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer