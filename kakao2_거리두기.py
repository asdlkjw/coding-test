def solution(places):
    answer = []
    for place in places:
        for i,plc in enumerate(place):
            tmp = 0
            for j,fp in enumerate(plc):
                if fp.count('P'):
                    if i != 0:
                        if place[i-1][j].count('P'):
                            answer.append(0)
                            tmp = 1
                            break
                        if place[i-1][j].count('O'):
                            if (i-1) != 0:
                                if place[i-2][j].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if j != 0:
                                if place[i-1][j-1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if j != 4:
                                if place[i-1][j+1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                    if i != 4:
                        if place[i+1][j].count('P'):
                            answer.append(0)
                            tmp = 1
                            break
                        if place[i+1][j].count('O'):
                            if (i+1) != 4:
                                if place[i+2][j].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if j != 0:
                                if place[i+1][j-1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if j != 4:
                                if place[i+1][j+1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                    if j != 0:
                        if place[i][j-1].count('P'):
                            answer.append(0)
                            tmp = 1
                            break
                        if place[i][j-1].count('O'):
                            if (j-1) != 0:
                                if place[i][j-2].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if i != 0:
                                if place[i-1][j-1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break 
                            if i != 4:
                                if place[i+1][j-1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                    if j != 4:
                        if place[i][j+1].count('P'):
                            answer.append(0)
                            tmp = 1
                            break
                        if place[i][j+1].count('O'):
                            if (j+1) != 4:
                                if place[i][j+2].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if i != 0:
                                if place[i-1][j+1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
                            if i != 4:
                                if place[i+1][j+1].count('P'):
                                    answer.append(0)
                                    tmp = 1
                                    break
            if tmp == 1:
                break
        if tmp == 0:
            answer.append(1)        
    return answer