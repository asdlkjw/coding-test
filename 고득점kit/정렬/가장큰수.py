def solution(numbers):
    numbers = [[(str(num)*4)[:4], len(str(num))] for num in numbers ]
    nums = (sorted(numbers,reverse = True))
    return str(int(''.join([num[0][:num[1]] for num in nums])))

# 한자리수를 4자리수로 바꿔주는것이 포인트였다  int str 다시 써주는건 0000 같은것을 0으로