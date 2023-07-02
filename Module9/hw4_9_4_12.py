def discount_price(discount):
    result = 1 - discount

    def price_discount(price):

        new_price = price * result

        return new_price
    return price_discount


cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))
