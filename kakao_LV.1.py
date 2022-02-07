def solution(new_id):
    answer = ''
    # 1.소문자
    new_id = new_id.lower()
    # 2.-_. 빼고 삭제
    tmp = []
    for x in new_id:
      print(x)
      if x == "." or x == "-" or x == "_":
        tmp.append(x)
      elif x.isalnum() :
        tmp.append(x)
      else:
        pass
    new_id = ''.join(tmp)
    print(new_id)
    # 3... 중복 .
    cn = new_id.count('.')
    print(cn)
    for i in range(cn):
        if cn == i or cn == 1:
            break
        new_id = new_id.replace(f"{'.'*(i+2)}", '.')
    # 4.처음 마지막 . 제거
    print(new_id)
    new_id = new_id.strip('.')
    # 5.빈문자열제거
    print(len(new_id))
    if len(new_id) == 0:
      new_id = ''.join('a')
    # 6. 15까지
    print(new_id)
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
      
    # 7.아이디 길이 2자 이상 마지막 붙임
    if len(new_id) < 3:
        add = 3-len(new_id)
        new_id = f'{new_id+(new_id[-1])*add}'

    answer = new_id
    print(answer)

    return answer

solution('abcdefghijklmn.p')



import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st, print(st)
    


solution('abcdefghijklmn.p')