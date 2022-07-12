def solution(A):
    for number in set(A):
        if A.count(number) > len(A) / 2:
            return A.index(number)

    return -1