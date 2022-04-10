def solution(citations):
    import numpy as np
    citations = sorted(citations)
    median = (np.median(citations))
    w = (citations.index(median))
    while True:
        down, up = False, False
        if citations[w] <= len(citations[w:]):
            w -= 1
            down = True
        if citations[w] >= len(citations[:w]):
            w += 1
            up = True
        if (down == True) and (up == True):
            return citations[w]
    