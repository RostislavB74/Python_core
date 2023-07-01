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

        for i in range(0, n+1):
            if i not in cache:
                if i == 0:
                    cache[0] = 0
                    continue

                if i <= 1:
                    cache[i] = 1
                    continue
                print(f'i={i}')
                print(cache[i-1])
                cache[i] = cache[i-1] + cache[i-2]
                print(cache)

                print(f'hard work {n}')
        else:
            print(f'easy work {n}')
        return cache.values()
    return inner


def main():
    data = {0: 0, 1: 1, 2: 3, 3: 5, 4: 8, }
    calc = get_cache()
    print(calc(6))
    # print(calc(5))
    # print(calc(10))
    # print(calc(10))
    # print(calc(15))
    # print(calc(10))
    # print(calc(5))


if __name__ == '__main__':
    main()
