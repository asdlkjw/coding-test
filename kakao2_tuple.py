def solution(s):
    answer = []
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    print(s)
    
    count = []
    for i in s:
        i = ''.join(i.split(','))
        count.append(len(i))
    
    for i in range(len(count)):
        count2 = count.sort()
        
    return answer