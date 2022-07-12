
def solution(A, K):
    if K == 0 or len(A) <= 1:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]