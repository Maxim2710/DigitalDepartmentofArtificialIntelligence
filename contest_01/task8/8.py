def calculate_bills(N):
    denominations = [5000, 1000, 500, 200, 100]
    result = [0] * len(denominations)

    for i, denom in enumerate(denominations):
        if N == 0:
            break
        result[i] = N // denom
        N -= result[i] * denom

    return result


N = int(input().strip())
result = calculate_bills(N)
print(" ".join(map(str, result)))
