price = 100


def discount_price(discount):
    result = price * (1 - discount)
    print(result)
    return result


DISCOUNT = {
    'cost_15': 0.15,
    'cost_10': 0.1,
    'cost_05': 0.05
}


def main():
    calc = discount_price()
    print(calc(0.15))
    print(calc(0.10))
    print(calc(0.05))


cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)


if __name__ == '__main__':
    main()
