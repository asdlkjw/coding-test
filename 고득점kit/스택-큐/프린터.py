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



import collections
def popleft_loc_prior(locations_dict, priorities_dict):
    return locations_dict.popleft(), priorities_dict.popleft()

def append_loc_prior(locations_dict, priorities_dict, loc, prior):
    locations_dict.append(loc)
    priorities_dict.append(prior)

def solution(priorities, location):
    locations_dict  = collections.deque([i for i in range(len(priorities))])
    priorities_dict = collections.deque(priorities)

    i_print = 0
    while True:
        loc, prior = popleft_loc_prior(locations_dict, priorities_dict)
        if len(priorities_dict) != 0:
            if prior < max(priorities_dict):
                append_loc_prior(locations_dict, priorities_dict, loc, prior)
            else:
                i_print = i_print + 1
                if loc == location:
                    return i_print
        else:
            return i_print + 1