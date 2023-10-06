# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, account_number: str, balance: float ):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
       self.__balance += amount
       self.__balance -= self.__service_charge()
    
    def withdraw(self, amount: float):
        if self.__balance > amount:
            self.__balance -= amount
            self.__balance -= self.__service_charge()
        else:
            raise ValueError('You do not have enough money in the bank')
    def __service_charge(self):
        return self.__balance * 0.01
   
def main():
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(10)
    print(account.balance)
if __name__ == "__main__":
    main()
