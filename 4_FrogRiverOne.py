def solution(X, A):
    helper_array = set()

    for i in range (0, len(A)):
        if A[i] not in helper_array:
            helper_array.add(A[i])
        if len(helper_array) == X:
            return i

    return -1
    