def solution(A):
    if len(A) > 6:
        numbers = sorted(A)[-3:] + sorted(A)[:3]
    else:
        numbers = A
        
    res = float("-inf")
    for i in range(0, len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers)):
                if numbers[i] * numbers[j] * numbers[k] > res:
                    res = numbers[i] * numbers[j] * numbers[k]
                    
    return res