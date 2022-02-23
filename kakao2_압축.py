def solution(msg):
    import string
    answer = []
    alpha = list(string.ascii_uppercase)
    
    for i in (range(len(msg)-1)):
        if i == len(msg)-2:
            answer.append(alpha.index(msg[i+1])+1)
        else:
            try:
                answer.append(alpha.index(msg[i] + msg[i+1])+1)
                alpha.append(msg[i] + msg[i+1] + msg[i+2])
            except:
                answer.append(alpha.index(msg[i])+1)
                alpha.append(msg[i] + msg[i+1])
    return answer