class IncorrectGuessError(Exception):
    def __init__(self, differnce):
        super().__init__()
        self.differnce = differnce

class NumbetTooSmallError(IncorrectGuessError):
    print("Za mały numer")

class NumberTooBigError(IncorrectGuessError):
    print("Za duży numer")

def guess(number):
    number_to_guuess = 10
    if number > number_to_guuess:
        raise NumberTooBigError(number - number_to_guuess)
    elif number < number_to_guuess:
        raise NumbetTooSmallError(number_to_guuess - number)

    #if number == number_to_guuess:
    print("Brawo")

try:
    guess(5)
except NumberTooBigError as ntb:
    print("Za duża o {}".format(ntb.differnce))
except NumbetTooSmallError as nts:
    print("Za mała o {}".format(nts.differnce))