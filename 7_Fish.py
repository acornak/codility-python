def solution(A, B):
    if sum(B) == 0 or sum(B) == len(B):
        return len(B)   
    
    upstream = []
    res = 0

    for i in range (0, len(A)):
        if B[i] == 1:
            upstream.append(A[i])
        else:
            while len(upstream) > 0:
                if upstream[-1] < A[i]:
                    upstream.pop()
                else:
                    break
            else:
                res += 1

    res += len(upstream)
    return res