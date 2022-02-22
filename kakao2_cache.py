def solution(cacheSize, cities):
    answer = 0        
    cache = []
    for city in cities:
        city = city.upper()
        if cacheSize == 0:
            answer += 5        
        elif not city in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
        
    return answer

#### LRU 알고리즘 배우기