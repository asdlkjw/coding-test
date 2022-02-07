# replace 를 사용하면 if 문을 간결하게 할 수 있다.
def solution(s):
  eng = {
      'zero':0,
      'one':1,
      'two':2,
      'three':3,
      'four':4,
      'five':5,
      'six':6,
      'seven':7,
      'eight':8,
      'nine':9
      }
  try:
      answer = int(s)
  except:
      answer = [] 
      b = 0
      for i in range(len(s)):
        i = i+b
        if i == len(s):
          break
        try:
          answer.append(int(s[i]))    
        except:
          if s[i:i+3] in eng.keys() :
            answer.append(eng[s[i:i+3]])
            b += 2
          elif s[i:i+4] in eng.keys():
            answer.append(eng[s[i:i+4]])
            b += 3
          elif s[i:i+5] in eng.keys():
            answer.append(eng[s[i:i+5]])
            b + 4
                  
      answer = ''.join(str(_) for _ in answer)      
  return answer

print(solution("one4seveneight"))