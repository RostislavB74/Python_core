DEFAULT_DISCOUNT = 0.05
customer_list = [{'name': "Dima"}, {'name': 'Boris', 'discount': 0.15}]
price = 10


def get_discount_price_customer(price, customer):

    # for customer_dict in customer_list:
    for keys in customer:
        if customer[keys]:
            try:
                price = price * (1 - customer['discount'])
            except KeyError:
                price = price * (1 - DEFAULT_DISCOUNT)
            return price


# customer = {'name': "Dima"}
customer = {'name': 'Boris', 'discount': 0.15}
print(get_discount_price_customer(price, customer))
