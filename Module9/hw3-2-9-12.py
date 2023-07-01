def caching_fibonacci(cache=None):
    # print(cache)
    if cache is None:
        cache = {}

    def fibonacci(n):
        if n not in cache:
            if n <= 1:
                cache[n] = n
                # print(cache)
                return cache[n]
            else:
                # print(cache.values())
                cache[n] = fibonacci(n-1)+fibonacci(n-2)
                return fibonacci(n-1)+fibonacci(n-2)
        return cache[n]

    return fibonacci


def main():
    calc = caching_fibonacci()
    print(calc(0))
# print(calc(0))
    print(calc(5))
    # print(calc(2))


if __name__ == '__main__':
    main()
