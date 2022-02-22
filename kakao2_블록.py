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
                if (df[i+1][j] == 1):
                    board[i+1][j] = board[i][j]
                    board[i][j] = '0'
        for a in range(m):            
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == '0':
                        board[i+1][j] = board[i][j]
                        board[i][j] = '0'                    

        for i in range(m):
            for j in range(n):
                if df[i][j] == 1:
                    answer += 1
    return answer


def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    # set_board
    for i, j in pop_set:
        b[i][j] = 0        
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)
     
def solution(m, n, board):
    count = 0
    b = list(map(list,zip(*board)))
    while True:
        pop = pop_num(b, m, n)
        if pop == 0: return count
        count += pop