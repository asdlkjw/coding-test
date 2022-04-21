def solution(prices):
    answer = []
    room  = [0]*len(prices)
    for i in range(len(prices)):
        for price in prices[i+1:]:
            if i <= price:
                room[i] += 1
            else:
                continue
    print(room)
    return answer