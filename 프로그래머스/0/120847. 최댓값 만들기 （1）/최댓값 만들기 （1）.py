def solution(numbers):
    a = sorted(numbers)
    l = len(a)
    answer = a[l-1] * a[l-2]
    return answer