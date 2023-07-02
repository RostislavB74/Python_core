price = 100


def discount_price(discount):
    result = price * (1 - discount)
    print(result)
    return result


# def main():
    # calc = discount_price()
    # print(cost_15(15))
    # print(cost_10(10))
    # print(cost_05(5))
DISCOUNT = {"cost_15": 0.15, "cost_10": 0.10, "cost_05": 0.05}


def get_handler(discount):
    return DISCOUNT[discount]


handler_15 = get_handler("cost_15")
handler_10 = get_handler("cost_10")
handler_05 = get_handler("cost_05")


cost_15 = discount_price(handler_15)
cost_10 = discount_price(handler_10)
cost_05 = discount_price(handler_05)


# if __name__ == '__main__':
#     main()
