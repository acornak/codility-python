def solution(A):
    A = sorted(A)
    return abs(sum(A[::2]) - sum(A[1::2]))