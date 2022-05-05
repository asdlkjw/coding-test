def solution(people, limit):
    tmp = []
    for i,weight in enumerate(people):
        if weight <= (limit/2):
            tmp.append(weight)
    for i in tmp:
        people.pop(people.index(i))
    answer = len(people)
    
    print(people)
    for l in tmp:
        for w in people:
            if w <= (limit - l):
                answer += 1
                print('aaaaaa')
                
    print(len(tmp)/2)
    return answer