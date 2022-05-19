def solution(bridge_length, weight, truck_weights):
    answer = 0
    import queue
    que = queue.Queue()
    now = 0
    for truk in truck_weights:
        if weight - now <= truk:
            que.put(truk)
            
        
    for _ in range(len(truck_weights)):
        # (que.get())
        pass
    
    print(sum(que))
    return answer