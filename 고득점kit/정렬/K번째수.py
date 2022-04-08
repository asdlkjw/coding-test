def solution(array, commands):     
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]
    #11:15분 스타트 #11:21분 종료