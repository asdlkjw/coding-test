def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)
    for i in range(0,len(scoville),2):
        try:
            print(scoville[i], scoville[i+1])
            pass
        except:
            print(scoville[i])
            pass
    return answer