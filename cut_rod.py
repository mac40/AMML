def cutrod(p, n):
    if n == 0:
        return 0
    q = -1  # considering only positive prices
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cutrod(p, n - i))
    return q


def cutrod_cost(p, n, c):
    if n == 0:
        return 0
    q = p[n - 1]
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cutrod_cost(p, n - i, c) - c)
    return q


def dyn_cutrod(p, n, c):
    r = []
    r.append(0)
    for j in range(1, n + 1):
        q = p[j - 1]
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j - i] - c)
        r.append(q)
    return r[n]


def main():
    p = [1, 5, 8, 9, 10, 17, 17, 20, 23, 24]
    n = int(input("Length of the rod (between 0 - 10) = "))
    c = int(input("Cut cost = "))
    print("Cut without cost = {}".format(cutrod(p, n)))
    print("Cut with cost = {}".format(cutrod_cost(p, n, c)))
    print("Dynamic approach cut with cost = {}".format(dyn_cutrod(p, n, c)))

if __name__ == "__main__":
    main()
