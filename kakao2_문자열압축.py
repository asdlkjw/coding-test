def solution(s):
    answer = 0
    import re
    from collections import Counter
    a = {4}
    b = (re.findall(fr'[a-z]{a}',s))  
    print(b)
    print(Counter(b))
    
    return answer

def solution(s):
    answer=10000
    for n in range(1,len(s)//2+2):
        res=''
        cnt=1
        tmp=s[:n] #단위문자열 초기화

        for i in range(n,len(s)+n,n):
            if tmp == s[i:i+n]:
                cnt+=1
            else:
                if cnt==1:
                    res+=tmp
                else:
                    res+=str(cnt)+tmp
                tmp=s[i:i+n]
                cnt=1
        #print(res)
        answer=min(answer,len(res))
    return answer



###########베스트 풀이 ################ 별로임 코드 걍 복잡하기만 함 그냥 겉멋만 듬

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))