def solution(numbers):
    answer = ''
    print(str(numbers[1])[-3])
    return ''.join(sorted(map(str,numbers),reverse = True))