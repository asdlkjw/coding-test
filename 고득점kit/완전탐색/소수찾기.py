def getPrime(n):
    primes = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if primes[i] == True:
            for j in range(i+i, n, i):
                primes[j] = False
    return [i for i in range(2,n) if primes[i] == True]

def solution(numbers):
    import re
    from itertools import permutations
    pm = (re.findall('\d',numbers))
    temp = list()
    for p in range(1,len(pm)+2):
        tmp = (permutations(pm, p))
        temp.extend([int(''.join(i)) for i in (list(set(tmp)))])
    subprime = list(set(filter(lambda x: x>=2,temp)))
    prime = (getPrime(max(subprime)+1))
    return len([i for i in subprime if i in prime ])

#################################################################
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)