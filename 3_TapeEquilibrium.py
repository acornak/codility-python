def solution(A):
    first = sum(A[:1])
    second = sum(A[1:])
    diff = abs(first - second)

    for number in A[1:]:
        first = first + number
        second = second - number
        if abs(first - second) < diff:
            diff = abs(first - second)
    
    return diff

# something is not correct here