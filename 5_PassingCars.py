def solution(A):
    east = 0
    res = 0


    for index, val in enumerate(A):
        if res > 1000000000:
            return -1
        if val == 0:
            east += 1
        else:
            res += east

    return res