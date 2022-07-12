def solution(A):
    disc_start = []
    disc_end = []
    for index, val in enumerate(A):
        disc_start.append(index - val)
        disc_end.append(index + val)

    disc_start.sort()
    disc_end.sort()

    open_discs = 0
    k = 0
    res = 0

    for i in range(len(A)):
        for j in range(k, len(A)):
            if disc_start[i] <= disc_end[j]:
                res += open_discs
                if res > 10000000:
                    return -1
                open_discs += 1
                break
            k += 1
            open_discs -= min(1, open_discs)

    return res