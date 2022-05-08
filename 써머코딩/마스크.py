def solution(atmos):
    answer = 0
    mask = [0] * len(atmos)
    for at, mos in enumerate(atmos):
        i,j = mos
        if (80 < i < 151) or (35 < j < 76):
            if (mask[at-1] in (0, 2, 3)) and (mask[at-2] in (0, 2, 3)):
                mask[at] += 1

        elif (150 < i) and (75 < j):
            if mask[at-1] == 1 or mask[at-2] == 1:
                mask[at] = 3 
            else:
                mask[at] = 2

    for i in mask:
        if 0< i <3:
            answer += 1
    return answer