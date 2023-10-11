# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def _validate_day(self):
        if self.__day in range (1, 30 +1):
            return self.__day

    def _validate_month(self):
        if self.__month in range (1, 12 +1):
            return self.__month
    
    def _validate_year(self):
        if len(str(self.__year)) == 4 and str(self.__year).isdigit():
            return self.__year
    def _validate_another_day(self, another):
        if another.__day in range (1, 30 +1):
            return another.__day
    def _validate_another_month(self, another):
        if another.__month in range (1, 12 +1):
            return another.__month
    def _validate_another_year(self, another):
        if len(str(another.__year)) == 4 and str(another.__year).isdigit():
            return another.__year

    def _self_date(self):
        tuple_self_date = (self._validate_day(), self._validate_month(), self._validate_year())
        return tuple_self_date
    def _another_date(self, another):
        tuple_another_date = (self._validate_another_day(another), self._validate_another_month(another), self._validate_another_year(another))
        return tuple_another_date
    
    def __eq__(self, another):
       return self._self_date() == self._another_date(another)
    
    def __ne__(self, another):
        return self._self_date() != self._another_date(another)
    
    def __lt__(self, another):

        if self._validate_year() < self._validate_another_year(another):
            return True    
        elif  self._validate_year() == self._validate_another_year(another):
            if self._validate_month() < self._validate_another_month(another):
                return True
            elif self._validate_month() == self._validate_another_month(another):
                if self._validate_day() < self._validate_another_day(another):
                    return True
                else:
                    return False
        else:
            return False
    
    def __gt__(self, another):

        if self._validate_year() > self._validate_another_year(another):
            return True
        elif  self._validate_year() == self._validate_another_year(another):

            if self._validate_month() > self._validate_another_month(another):

                return True
            elif self._validate_month() == self._validate_another_month(another):
    
                if self._validate_day() > self._validate_another_day(another):
                    return True
                else:
                    return False
        else:

            return False


def main():
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(5, 6, 1876)
    d3 = SimpleDate(6, 6, 1876)

    # print(d1)
    # print(d2)
    
    # print(d1 == d2)
    # print(d1 != d2)
    # print(d1 == d3)
    print(d2 < d2)
    print(d2 > d3)
if __name__ == "__main__":
    main()