# def caching_fibonacci(n):
#     if n<=1:
#         return n
#     def inner(n):
#         if n not in cache:
#             cache(n) =
#         return inner

# n = 5


def get_cache(cache=None):
    if cache is None:
        cache = {}

    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum([i for i in range(1, n+1)])
            print(f'hard work {n}')
            return cache[n]
        else:
            print(f'easy work {n}')
            return cache[n]
    return inner


def main():
    data = {5: 15, 10: 55, 15: 120}
    calc = get_cache(data)
    print(calc(5))
    print(calc(5))
    print(calc(10))
    print(calc(10))
    print(calc(15))
    print(calc(10))
    print(calc(5))


if __name__ == '__main__':
    main()
