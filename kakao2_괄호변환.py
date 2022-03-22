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
                
                if right(u) == True:
                    if x == '':
                        return u
                    x = dive(x)
                    w = u + x   
                    return w
                
                else:
                    x = dive(x)
                    y = ''
                    for i in u[1:-2]:
                        if i == ')':
                            y += '('
                        else:
                            y += ')'
                    w = '(' + x + ')' + y
                    return w
    answer = dive(p)
    print(answer)
                
                
        
    return answer