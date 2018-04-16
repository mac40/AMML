# O(n^2)
def F(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)


# O(n)
def fibonacci(n, a = 0, b = 1):
    if n == 1:
        print(a)
        return a
    return fibonacci(n - 1, b, a + b)


def main():
    number = int(input("Fibonacci position: "))
    result = fibonacci(number)
    # result2 = F(number)
    # print("F result = {}".format(result2))
    print(result)


if __name__ == "__main__":
    main()
