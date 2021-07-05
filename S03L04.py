def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(function,values):
    for x in values:
        print("Result of {} with {} is {}".format(function.__name__,x,function(x)))


x_table=list(range(11))

generate_values(double,x_table)
generate_values(square, x_table)
generate_values(negative, x_table)
generate_values(div2, x_table)