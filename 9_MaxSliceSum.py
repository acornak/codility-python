def solution(A):
    max_ending = 0
    max_slice = float("-inf")

    for number in A:
        max_ending = max(float("-inf"), max_ending + number)
        max_slice = max(max_slice, max_ending)

    return max_slice

# only 53 percent correctness