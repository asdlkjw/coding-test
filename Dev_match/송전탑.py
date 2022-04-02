n	edges	k	a	b	result
8	[[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]	4	0	3	7

def solution(n, edges, k, a, b):
    answer = -1
    tmp= []
    for j,i in enumerate(edges):
        try:
            if i.index(int(b)):
                print(j,i)
        except:
            pass
    print(tmp)
    return answer