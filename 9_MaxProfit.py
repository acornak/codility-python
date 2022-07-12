def solution(A):
    min_price = float("inf")
    profit = 0

    for price in A:
        min_price = min(price, min_price)
        profit = max(price - min_price, profit)

    return profit