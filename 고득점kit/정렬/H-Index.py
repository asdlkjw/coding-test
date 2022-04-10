def solution(citations):
    import numpy as np
    citations = sorted(citations)
    median = (np.median(citations))
    w = (citations.index(median))
    print(citations)
    print(w, 'df', median)
    for _ in range(99):
        if citations[w] > len(citations[w:]):
            w -= 1
        elif citations[w] < len(citations[w:]):
            w += 1
        elif citations[w] == len(citations[w:]):
            return citations[w]
    return citations[w]