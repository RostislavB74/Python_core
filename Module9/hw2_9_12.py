DEFAULT_DISCOUNT = 0.05
customer = [{'name': "Dima"}, {'name': 'Boris', 'discount': 0.15}]
price = 100


def get_discount_price_customer(price, customer):
    for elem in customer:
        for keys in elem:
            if keys == 'discount':
                if elem[keys]:
                    price = price * (1 - elem['discount'])
                    return price
            price = price * (1 - DEFAULT_DISCOUNT)
            # if key and values:

            #     price = price * (1 - )
        return price


print(get_discount_price_customer(price, customer))
