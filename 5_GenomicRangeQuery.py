def solution(S, P, Q):
    res = len(P) * [0]

    for i in range (0, len(P)):
        substr = S[P[i]:Q[i]]+S[Q[i]]
        if "A" in substr:
            res[i] = 1
        elif "C" in substr:
            res[i] = 2
        elif "G" in substr:
            res[i] = 3
        else:
            res[i] = 4

    return res

