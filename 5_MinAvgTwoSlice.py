def solution(A):
    min_avg_value = (A[0] + A[1]) / 2
    min_avg_position = 0

    for i in range(1, len(A) - 2):
        if (A[i] + A[i+1]) / 2 < min_avg_value:
            min_avg_value = (A[i] + A[i+1]) / 2
            min_avg_position = i
        if (A[i] + A[i+1] + A[i+2]) / 3 < min_avg_value:
            min_avg_value = (A[i] + A[i+1] + A[i+2]) / 3
            min_avg_position = i

        
    if (A[-1] + A[-2]) / 2 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2
        min_avg_position = len(A)-2

    return min_avg_position
