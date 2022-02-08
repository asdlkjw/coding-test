
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
answer = []
answer2 = []
stages2 = range(1,N+1)
for i in stages2:
  answer2.append(stages.count(i)/len([j for j in stages if (j >= i)] ))
for i in answer2:
  answer.append(answer2.index(max(answer2))+1)
  answer2[answer2.index(max(answer2))] = -1

print(answer)
