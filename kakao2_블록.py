N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

df = [[0] * N for _ in range(N)] 
df[0][0] = 1

for i in range(N):
    for j in range(N):
        if (i is N-1) & (j is N-1): 
            print(df[i][j])
            break
        tmp = field[i][j]
        if j + tmp < N:
            df[i][j + tmp] += df[i][j]
        if i + tmp < N:
            df[i + tmp][j] += df[i][j]

def solution(m, n, board):
    answer = 0
    df = [[0]*n for i in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            if (board[i][j+1] is board[i+1][j]) and (board[i+1][j+1] is board[i][j]) and (board[i+1][j] is board[i][j]):
                df[i][j] = 1
                df[i+1][j] = 1
                df[i][j+1] = 1
                df[i+1][j+1] = 1
    print(df)
    
    for i in range(m-1):
        for j in range(n):    
            if (df[i+1][j] == 1) and (board[i][j] != 0):
                print(board[i][j])
                
    
#     print(board)
    return answer