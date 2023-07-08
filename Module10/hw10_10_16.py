from collections import UserList
payment = [1, -3, 4]


class AmountPaymentList(UserList):
    def amount_payment(self):

        sum = 0
        for value in payment:
            if value > 0:
                sum = sum + value
        print(sum)
        return sum
