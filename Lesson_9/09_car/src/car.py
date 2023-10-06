# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__amount_of_petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__amount_of_petrol = 60
    
    def drive(self, km:int):
         if km <= self.__amount_of_petrol:
            self.__amount_of_petrol -= km
            self.__odometer += km

    def __str__(self):
        return f"Car: odometer reading {self.__odometer}, top speed: {self.__amount_of_petrol}"

def main():
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car) 

if __name__ == "__main__":
    main()