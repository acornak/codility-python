def solution(A):
    expected_sum = len(A) * ((len(A) + 1)/2)
    if sum(A) == expected_sum and len(set(A)) == len(A):
        return 1
    return 0