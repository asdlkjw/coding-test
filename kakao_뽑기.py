def solution(board, moves):
    box = []
    count = 0
    for x,y in enumerate(moves):
        for i in board:
            if i[y-1] != 0:
                box.append(i[y-1])
                i[y-1] = 0
                break
            else:
                pass

        if len(box) >= 2:
            if (box[-1] == box[-2]):
                box = box[:-2]
                count += 1
    return count*2