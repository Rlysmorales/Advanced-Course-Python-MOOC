# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observation_list = []

    def add_observation(self, observation: str):
        self.__observation_list.append(observation)
    
    def latest_observation(self):
        if self.__observation_list == 0:
            return f"Empty List"
        else:
            return str(self.__observation_list[len(self.__observation_list) - 1])
           
    def number_of_observations(self):
        total_number = len(self.__observation_list)
        return total_number
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

def main():
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    a=WeatherStation("Kumpula")
    a.latest_observation()    

    print(station.number_of_observations())
    print(station)
if __name__ == "__main__":
    main()