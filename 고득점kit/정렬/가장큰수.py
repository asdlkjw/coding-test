def solution(numbers):
    numbers = [[(str(num)*4)[:4], len(str(num))] for num in numbers ]
    nums = (sorted(numbers,reverse = True))
    return ''.join([num[0][:num[1]] for num in nums])