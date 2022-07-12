def solution(N):
    i = 1
    helper = []
    while (i * i < N):
        if N % i == 0:
            helper.append(i)
        i += 1
    if (i * i == N):
        helper.append(i)

    perimeter = float("inf")

    for number in helper:
        if 2 * (number + N / number) < perimeter:
            perimeter = 2 * (number + N / number)

    return int(perimeter)