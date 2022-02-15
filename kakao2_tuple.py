def solution(s):
    answer = []
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    print(s)
    
    count = []
    for i in s:
        i = ''.join(i.split(','))
        count.append(int(i))
    print(count)
    for k in s:
        for i,j in enumerate(count):
            if min(count) == j:
                answer.append((s[i]))
                print(count)
                del count[i]
                continue
            
    print(count)
    print(answer)
    return answer