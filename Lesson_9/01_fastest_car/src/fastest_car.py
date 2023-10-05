# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:

def fastest_car(cars: list):

    empty_dic = {"make":"", "top_speed": 0}
    saved_list = 0
    for car in cars:
        if car.top_speed > saved_list:
            saved_list = car.top_speed 
            empty_dic["make"] = car.make
            empty_dic["top_speed"] = car.top_speed
    return empty_dic["make"]

def main():
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))

if __name__ == "__main__":
    main()