class DateError(Exception):
    pass

class InvalidYearError(DateError):
    pass

class InvalidMonthError(DateError):
    pass

class InvalidDayError(DateError):
    pass

class Date:
    def __init__(self, day, month, year):
        if not isinstance(year, int):
            raise InvalidYearError
        elif not isinstance(month, int) or month > 12 or month < 1:
            raise InvalidMonthError
        else:
            if not isinstance(day, int):
                raise InvalidDayError 
            elif month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
                raise InvalidDayError
            elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
                raise InvalidDayError
            elif month == 2 and (day < 1 or day > 28):
                raise InvalidDayError

        self.year = year
        self.month = month
        self.day = day

date = Date(30, 5, 2020)
assert date.day == 30
assert date.month == 5
assert date.year == 2020

try:
    date2 = Date(40, 5, 2020)
except InvalidDayError:
    print("Niepoprawny dzień")
except InvalidYearError:
    print("Niepoprawny rok")
except InvalidMonthError:
    print("Niepoprawny miesiąc")
else:
    print('Bez błędu, a trzeba było :(')



  

