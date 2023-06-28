DEFAULT_DISCOUNT = 0.05
customer_list = [{'name': "Dima"}, {'name': 'Boris', 'discount': 0.15}]
price = 100


def get_discount_price_customer(price, customer):
    for customer in customer_list:
        for keys in customer:
            name = keys[0]
            if keys == 'discount':
                if customer_list[keys]:
                    price = price * (1 - customer_list['discount'])
                    print(f'{name}: {price}')
            else:

                price = price * (1 - DEFAULT_DISCOUNT)
                print(f'{name}: {price}')
            continue
            # if key and values:

            #     price = price * (1 - )
    return price


customer = 'Dima'
print(get_discount_price_customer(price, customer))
