def solution(A):
    A = set(A)
    count = 1
    while count in A:
        count += 1
    return count