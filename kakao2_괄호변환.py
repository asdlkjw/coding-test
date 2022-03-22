def solution(p):
    answer = ''
    if p == answer:
        return answer
    
    def right(u):
        a ,b = 0, 0
        for i in u:
            if i == '(':
                a += 1
            else:
                b += 1
            if a < b:
                return False
        return True
                
                
    
    def dive(v):
        if v == '':
            return ''
        for i in range(2, len(v)+2, 2):
            if (v[:i]).count('(') == v[:i].count(')'):
                u, x = v[:i], v[i:]   
                print(u, x)
                if right(u) == True:
                    if x == '':
                        return u
                    x = dive(x)
                    w = u + x   
                    return w      
                else:
                    x = dive(x)
                    y = ''
                    for i in u[1:-1]:
                        if i == ')':
                            y += '('
                        else:
                            y += ')'
                    w = '(' + x + ')' + y
                    return w
                
    answer = dive(p)
    print(answer)
                
                
        
    return answer


##########best 풀이#################### 

def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))