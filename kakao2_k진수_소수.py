def isprime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True
### 소수 판별 알고리즘 ###
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
        if int(i) != 1 and isprime(int(i)) == True:
            answer += 1
    return answer

### v