def solution(X, Y, D):
    distance = Y - X
    if distance == 0 or D == 0:
        return 0
        
    return distance // D if distance % D == 0 else distance // D