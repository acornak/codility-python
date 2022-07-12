def solution(S):
    if len(S) %2 != 0:
        return 0
        
    helper_list = []

    for bracket in S:
        if bracket == "(":
            helper_list.append(str(bracket))
        elif len(helper_list) > 0 and bracket == ")":
            helper_list.pop(-1)
        else: 
            return 0

    if len(helper_list) == 0:
        return 1
    
    return 0