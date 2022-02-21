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