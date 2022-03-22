def solution(p):
    answer = ''
    if p == answer:
        return answer
    
    def dive(v):
        if v == '':
            return ''
        for i in range(2, len(v)+2, 2):
            if (v[:i]).count('(') == v[:i].count(')'):
                u, x = v[:i], v[i:]   
                if x == '':
                    return u
                
                if u == True:
                      x = dive(x)
                    w = u + x   
                    return w
            
    
    for i in range(2,len(p)+2, 2):
        if (p[:i].count('(') == p[:i].count(')')):
            u ,v = p[:i], p[i:]
            
            if u == True:
                u, v = dive(v)
                
            else:
                
                '(' + v ')' + reverse u[1:-2]
                
                
        
    return answer