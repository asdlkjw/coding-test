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
        # 회사 노트북 반납으로 인한 당분간 1일1커밋은 못할듯 잠정 중단... 텀퓨터 하나 사야지
    return answer