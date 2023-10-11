# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def _adding_self(self):
        leading_zero_self = f".{self.__cents:02d} "
        self_int = float(leading_zero_self)
        
        return self.__euros + self_int
    
    def _adding_another(self, another):
        leading_zero_another = f".{another.__cents:02d} "
        another_int = float(leading_zero_another)
        
        return another.__euros + another_int
    
    def __eq__(self, another):
       return self._adding_self() == self._adding_another(another)
    
    def __ne__(self, another):
        return self._adding_self() != self._adding_another(another)
    
    def __lt__(self, another):
        return self._adding_self() < self._adding_another(another)
    
    def __gt__(self, another):
        return self._adding_self() > self._adding_another(another)
    
    def __add__(self, another):
        # leading_zero_self = f".{self.__cents:02d} "
        # leading_zero_another = f".{another.cents:02d} "
        # self_int = float(leading_zero_self)
        # another_int = float(leading_zero_another)
        
        # addition_self = self.__euros + self_int
        # addition_another = another.euros + another_int
        # addition = addition_self +  addition_another 
        addition = self._adding_self() + self._adding_another(another)
        return f"{addition:.2f} eur"
        
    
    def __sub__(self, another):

        if (self._adding_self() - self._adding_another(another)) <= 0:
            raise ValueError("a negative result is not allowed")
        else:
            subtract = self._adding_self() - self._adding_another(another)
            return f"{subtract:.2f} eur"





def main():
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e4)

    e5 = e2-e1
    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
    print(e5)
    
if __name__ == "__main__":
    main()