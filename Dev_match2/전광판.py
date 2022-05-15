def solution(n, text, second):
    answer = '_'*n
    text = text.replace(' ', '_')
    i = 0
    j = 0
    while j != second:
        if i < n:
            answer = (answer[1:n-i] + text[:i+1])
        elif i >= n:
            answer = answer[1:] + '_'*(1)
        i += 1
        j += 1
        if (i % (2*n)) == 0:
            i = 0
    return answer