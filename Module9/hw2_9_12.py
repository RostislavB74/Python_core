DEFAULT_DISCOUNT = 0.05
customer_list = [{'name': "Dima", 'discount': 0.0},
                 {'name': 'Boris', 'discount': 0.15}]
price = 100


def get_discount_price_customer(price, customer):

    if customer in customer_list:
        print(customer)
        if customer_list['discount']:
            price = price * (1 - customer_list['discount'])
    price_discout = price * (1 - DEFAULT_DISCOUNT)
    return customer_list['name'], price_discout

#   if keys == 'discount':
#             if customer_list[keys]:
#                 price = price * (1 - customer_list['discount'])
#                 print(f'{name}: {price}')
#         else:

#             price = price * (1 - DEFAULT_DISCOUNT)
#             print(f'{name}: {price}')
#         continue
#         # if key and values:

#         #     price = price * (1 - )
# return price


customer = 'Boris'
print(get_discount_price_customer(price, customer))
