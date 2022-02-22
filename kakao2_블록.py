def solution(m, n, board):
    answer = 0

    for i,j in enumerate(board):
        board[i] = '.'.join(j)
        board[i] = board[i].split('.')
        
    for k in range(20):
        df = [[0]*n for i in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                if (board[i][j-1] is board[i-1][j]) and (board[i-1][j-1] is board[i][j]) and (board[i-1][j] is board[i][j]) and (board[i][j] != '0'):
                    df[i][j] = 1
                    df[i-1][j] = 1
                    df[i][j-1] = 1
                    df[i-1][j-1] = 1
        for i in range(m-1):
            for j in range(n):    
                if (df[i+1][j] == 1) and (board[i][j] != '0'):
                    board[i+1][j] = board[i][j]
                    board[i][j] = '0'

        for i in range(m):
            for j in range(n):
                if df[i][j] == 1:
                    answer += 1
    return answer