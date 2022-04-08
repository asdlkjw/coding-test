def solution(numbers):
    numbers = [[(str(num)*4)[:4], len(str(num))] for num in numbers ]
    nums = (sorted(numbers,reverse = True))
    return ''.join([num[0][:num[1]] for num in nums])

# 한자리수를 4자리수로 바꿔주는것이 포인트였다