def solution(s):
    answer = 0
    import re
    from collections import Counter
    a = {4}
    b = (re.findall(fr'[a-z]{a}',s))  
    print(b)
    print(Counter(b))
    
    return answer

def solution(s):
    answer=10000
    for n in range(1,len(s)//2+1):
        res=''
        cnt=1
        tmp=s[:n] #단위문자열 초기화

        for i in range(n,len(s)+n,n):
            if tmp == s[i:i+n]:
                cnt+=1
            else:
                if cnt==1:
                    res+=tmp
                else:
                    res+=str(cnt)+tmp
                tmp=s[i:i+n]
                cnt=1
        #print(res)
        answer=min(answer,len(res))
    return answer