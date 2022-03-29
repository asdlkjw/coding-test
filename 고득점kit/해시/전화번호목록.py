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


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# 깔끔한 풀이  startswith 라는 함수를 활용  zip으로  한칸 밀어서 합쳐서 사용함