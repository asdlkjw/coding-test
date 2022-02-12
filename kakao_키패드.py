def solution(numbers, hand):
    answer = ''
    
    used_hand =[]
    left = [0,0]
    right = [0,0]
    
    pad = [['*',7,4,1],[0,8,5,2],['#',9,6,3]]
    
    for i in range(len(numbers)):
        for k,j in enumerate(pad):
            if numbers[i] in j:
                case = [k,j.index(numbers[i])]
                print(case)

        if numbers[i] in [1,4,7]:
            used_hand.append("L")
            left = case
        elif numbers[i] in [3,6,9]:
            used_hand.append("R")
            right = case
        else:
            a = [abs(x-y) for x,y in zip(case, left)]
            b = [abs(x-y) for x,y in zip(case, right)]
            
            print('a',a)
            print('b',b)
            
            if abs(sum(a)) < abs(sum(b)):
                used_hand.append("L")
                left = case
            elif abs(sum(a)) > abs(sum(b)):
                used_hand.append("R")
                right = case
            else:
                if hand == 'right':
                    used_hand.append("R")
                    right = case
                else:
                    used_hand.append("L")
                    left = case

    answer = ''.join(used_hand)
    return answer