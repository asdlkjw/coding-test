def solution(n, k):
    import re
    answer = 0

    knum = []
    while True:    
        n, m = n//k, n%k
        knum.append(m)
        if n == 0:
            break 
    knum =  ''.join(str(x) for x in knum[::-1])
    result = (re.findall(r'[^0]+', knum))
    for i in result:
        if int(i) != 1:
            answer += 1
    return answer