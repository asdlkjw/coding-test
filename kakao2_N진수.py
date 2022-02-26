def solution(n, t, m, p):
    import string
    answer = []
    result = []
    tmp = string.digits+string.ascii_lowercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r].upper()
        else :
            return convert(q, base) + tmp[r].upper()
    
    for i in range(t*m):
        result.append(convert(i, n))
        
    result = ''.join(result)
    
    for i in range(1,t+1): 
        answer.append(result[(m*i)-(m-p)-1])
        
    answer=''.join(answer)
    return answer