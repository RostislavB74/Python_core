def multiply (x):
    def inner(y):
        def func(z):
            return x*y*z
        return func
    return inner
multiply_ten = multiply(10)
multiply_10_3=multiply_ten(3)
multiply_10_3=4