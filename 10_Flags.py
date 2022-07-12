def solution(A):
    peaks = []
    for i in range (2, len(A)):
        if A[i-2] < A[i-1] > A[i]:
            peaks.append(i - 1)

    print(peaks)

