def solution(fees, records):
    answer = []
    record = []
    for i in records:
        record.append(i.split())
    for i in range(len(record)):
        h = int(record[i][0].split(":")[0])*60
        m = int(record[i][0].split(":")[1])
        record[i].append(h+m)
        
    for i in record:
        for j in record:
            if i[1] == j[1]:
                fee = round(fees[0]-abs(i[3]-j[3]), 0)
                print(fee)
    print(fees, record)
    ## 좀만 쉬자
    return answer