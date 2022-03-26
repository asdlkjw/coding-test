def solution(record):
    answer = []
    changename = ["Enter", "Change"]
    num = []
    uid = dict()
    for i in record:
        i = (i.split())
        if i[0] in changename:
            uid[f'{i[1]}'] = i[2]
        if i[0] != "Change":
            num.append(i[:2])
    for i in num:
        if i[0] == "Enter":
            answer.append(f'{uid[i[1]]}님이 들어왔습니다.')
        elif i[0] == "Leave":
            answer.append(f'{uid[i[1]]}님이 나갔습니다.')
    return answer