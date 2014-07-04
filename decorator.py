def decorator(F):
    def new_F(a, b):
        print ("input:", a, b)
        return F(a, b)

    return new_F


@decorator
def square_sum(a, b):
    return a ** 2 + b ** 2


@decorator
def square_diff(a, b):
    return a ** 2 - b ** 2


print (square_sum(3, 4))
print (square_diff(3, 4))