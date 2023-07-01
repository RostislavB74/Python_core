price = 100


def discount_price(discount):
    result = price * (1 - discount*0.01)
    print(result)
    return result

# def main():
    # calc = discount_price()
    # print(cost_15(15))
    # print(cost_10(10))
    # print(cost_05(5))


cost_15 = discount_price(15)
cost_10 = discount_price(10)
cost_05 = discount_price(5)


# if __name__ == '__main__':
#     main()
