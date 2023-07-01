price = 100


def discount_price(discount):
    result = price * (1 - discount)
    # print(result)
    return result


def main():
    # calc = discount_price()
    print(cost_15(price))
    print(cost_10(price))
    print(cost_05(price))


cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)


if __name__ == '__main__':
    main()
