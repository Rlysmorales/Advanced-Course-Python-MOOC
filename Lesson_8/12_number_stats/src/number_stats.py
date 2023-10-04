# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
    
    def add_number(self, number:int):
           self.count += 1
           self.numbers += number
    
    def count_numbers(self):
        return self.count
    
    def get_sum(self):
         if self.numbers == 0:
              return 0
         else:
              return self.numbers
         
    def average(self):
         try:
            return self.numbers / self.count
         except ZeroDivisionError:
             ...
    
def user_input():
    all_numbers = NumberStats()
    even_numbers = NumberStats()
    odd_numbers = NumberStats()

    while True: 
        user_input = int(input("Please type in integer numbers:"))
        if user_input % 2 == 0:
            even_numbers.add_number(user_input)   
        elif user_input < 0:
            print("Sum of numbers:", all_numbers.get_sum())
            print("Mean of numbers:", all_numbers.average())
            print("Sum of even numbers", even_numbers.get_sum())
            print("Sum of odd numbers", odd_numbers.get_sum())
            break
        elif user_input % 2 == 1:
            odd_numbers.add_number(user_input)

        if user_input >= 0: 
            all_numbers.add_number(user_input)

user_input()



