def solution(m, musicinfos):
    from datetime import datetime
    answer = '(None)'
    pan = []
    times_ = []
    for music in musicinfos:
        music = music.split(',')

        times = datetime.strptime(music[0], "%H:%M")
        times2 = datetime.strptime(music[1], "%H:%M")
        time = int((times2 - times).seconds / 60)
        
        mpl = len(music[-1])- music[-1].count('#')
        
        
        if time < mpl:
            alpha = music[-1][:time].count('#')
            if music[-1][time] == '#':
                alpha += 1
            tmp = music[-1][:time + alpha]
            if m in tmp:
                try:
                    if tmp[tmp.index(m)+len(m)] != "#":
                        answer = music[2]
                        pan.append(answer)
                        times_.append(time)
                    else:
                        if m in tmp[tmp.index(m)+len(m):]:
                            answer = music[2]
                            pan.append(answer)
                            times_.append(time)
                except:
                    answer = music[2]
                    pan.append(answer)
                    times_.append(time)
                    
        else:
            plus = music[-1][:(time%mpl)].count('#')
            if music[-1][(time%mpl)] == '#':
                plus += 1
            tmp = music[-1]*(int(time/mpl)) + music[-1][:(time%mpl)+plus]
            if m in tmp:            
                try:
                    if tmp[tmp.index(m)+len(m)] != "#":
                        answer = music[2]
                        pan.append(answer)
                        times_.append(time)
                    else:
                        if m in tmp[tmp.index(m)+len(m):]:
                            answer = music[2]
                            pan.append(answer)
                            times_.append(time)
                except:
                    answer = music[2]
                    pan.append(answer)
                    times_.append(time)

    if len(pan) > 1: 
        answer = pan[times_.index(max(times_))]
        if max(times_) == min(times_):
            answer = pan[0]
        
    return answer