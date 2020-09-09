n = 30
k = 3


def recur(n, k):
    if n < 2:
        return n
    else:
        return recur(n - 1, k) + recur(n - 2, k) * k

print(recur(n, k))