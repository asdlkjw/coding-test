print('go 2/9 8pm')

n =	5
arr1=	[9, 20, 28, 18, 11]
arr2=	[30, 1, 21, 17, 28]


a = []
b = []
for i in arr1:
  tmp = bin(i)[2:]
  a.append('0'*(n-len(tmp)) + f'{bin(i)[2:]}')
  
for i in arr2:
  tmp = bin(i)[2:]

  b.append('0'*(n-len(tmp)) + f'{bin(i)[2:]}')
    
print(a)
print(b)

ba = []
for j in range(n):
  aa = []
  for i in range(n):
    if (a[j][i] =="1" or b[j][i] == '1'):
      aa.append('#')
    else:
      aa.append(' ')
    
  print(aa)
  aa = ''.join(aa)
  print(aa)
  ba.append(aa)

print(ba)

print(["#####","# # #", "### #", "# ##", "#####"])

######################################################

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
print(solution(n, arr1, arr2))