def sum_numbers(*numbers):
    result = 0
    for x in numbers:
        result += x
    return result


def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

def kw_pw(*pwargs, **kwargs):
def com(a, e=12, *args, **kwargs):

result = sum_numbers(1,5,1,5,2,3)
print(result)

print_kwargs(a=5, b=3)