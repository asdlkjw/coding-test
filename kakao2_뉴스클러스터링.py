import re
def solution(str1, str2):
    
    str1_list = []
    str2_list = []
    str3_list = []
    str4_list = []    
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(0,len(str1)-1):
        str1_list.append((str1[i]+str1[i+1]))
        
    for i in range(0,len(str2)-1):
        str2_list.append((str2[i]+str2[i+1]))
    
    for i,strs in enumerate(str1_list):
        strs = re.sub(r"[^A-Z]","",strs)
        if len(strs) < 2:
            pass
        else:
            str3_list.append(strs)

            
    for i,strs in enumerate(str2_list):
        strs = re.sub(r"[^A-Z]","",strs)
        if len(strs) < 2:
            pass
        else:
            str4_list.append(strs)
            
    union = list(set(str3_list) | set(str4_list))
    intersection = list(set(str3_list) & set(str4_list))
    
    tmp = 0
    tmp2 = 0
    for inter in intersection:
        tmp += (min(str3_list.count(inter), str4_list.count(inter))-1)
        
    for uni in union:
        tmp2 += (max(str3_list.count(uni), str4_list.count(uni))-1)
        
    try:
        answer = ((len(intersection)+tmp)/(len(union)+tmp2))
    except:
        answer = 1

    return int(answer*65536)

###########################

import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

######## is alpha  함수 check

def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536