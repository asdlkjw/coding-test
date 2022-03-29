def solution(phone_book):
    answer = True
    temp = [len(i) for i in phone_book]
    temp_min = min(temp)
    temp_max = max(temp)
    if temp_max == temp_min: return True
    min_list = list()
    for i,j in enumerate(temp):
        if temp_min == j : min_list.append(i)
    for mn in min_list:
        tmp = phone_book[mn]
        for phone in phone_book:
            if phone == tmp: continue
            if tmp == phone[:temp_min]:
                answer = False 
                break
    return answer