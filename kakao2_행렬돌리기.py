def solution(rows, columns, queries):
    answer = []
    result =[[i for i in range(j,columns+j)] for j in range(1, (rows*columns), columns)]
    
    
    
    for querie in queries:
        querie = [i-1 for i in querie]


        save = [[],[],[],[]]

        for i in range(querie[1], querie[3]+1):
            save[0].append(result[querie[0]][i])
            save[2].append(result[querie[2]][i])

        for i in range(querie[0], querie[2]+1):
            save[1].append(result[i][querie[1]]) 
            save[3].append(result[i][querie[3]])
        
        for j,i in enumerate(range(querie[1], querie[3])):
            result[querie[0]][i+1] = save[0][j]
            result[querie[2]][i] = save[2][j+1]

        for j,i in enumerate(range(querie[0], querie[2])):
            result[i][querie[1]] = save[1][j+1]
            result[i+1][querie[3]] = save[3][j]
        save2 = []    
        for i in save:
            save2.append(min(i))
        answer.append(min(save2))

    return answer