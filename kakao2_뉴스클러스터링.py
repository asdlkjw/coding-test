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