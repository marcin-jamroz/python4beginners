def no_arg():
    return 5

def ident(x):
    return x

def mult(x, y):
    return x * y


def function_results_sum(*args, **kwargs):
    sum = 0
    for fun in args:
        if fun.__name__ in kwargs:
            tmp = kwargs[fun.__name__]

            if isinstance(tmp, int):
                sum += fun(tmp)
            else:
                sum += fun(*tmp)
        else:
            sum += fun()
    return sum

assert function_results_sum(no_arg, ident, mult, ident=2, mult=(3,4)) == 19
