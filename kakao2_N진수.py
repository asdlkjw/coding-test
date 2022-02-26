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

#########################

def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    for number in range(1, t*m):
        temp = []
        while number > 0:
            temp.append(data[number%n])
            number //= n
        numbers += "".join(reversed(temp))

    return numbers[p-1:t*m:m]  # 이 코드가 좀 괜찮은듯
