def solution(H):
    res = 0
    stack = []
    
    for height in H:
        while stack and height < stack[-1]:
            stack.pop()
        if not stack or height > stack[-1]:
            res += 1
            stack.append(height)

    return res