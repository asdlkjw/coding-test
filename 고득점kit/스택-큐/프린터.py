from collections import deque
def solution(priorities, location):
    answer = 0
    my_print = priorities[location]
    queue = deque(priorities)
    tmp = 0
    for i,j in enumerate(priorities):
        if j < max(list(queue)[1:]):
            if i == location:
                tmp += len(priorities[i:])
            else:
                # tmp -= 1
                pass
            
            queue.append(j)
            priorities.append(j)
            queue.popleft()
        else:
            if i == location:
                tmp += 1
                break
            print(j)
    print(tmp)
    return answer