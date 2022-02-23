def solution(msg):
    import string
    answer = []
    alpha = list(string.ascii_uppercase)
    tmp = 0
    for ms in range(1,len(msg)+1):
        if tmp == 0:
            pass
        else:
            tmp -= 1
            continue
        for i in range(ms,len(msg)+1):
            try:
                answer.append(alpha.index(msg[ms-1:i])+1)
                if (len((msg[ms-1:i]))-1) != 0:
                    answer.pop(-2)
                    tmp += 1 
            except:
                alpha.append((msg[ms-1:i]))

                break
    return answer


    def solution(msg):
    a = []
    msg += '_'
    s = list('_ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while len(msg) > 1:
        i = 0
        while msg[:-i] not in s:
            i += 1
        a += [s.index(msg[:-i])]
        s += [msg[:-i+1]]
        msg = msg[-i:]
    return a