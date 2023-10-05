# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.list_of_person = []
    
    def add(self, person: Person):
        self.list_of_person.append(person)

    def is_empty(self):
        if not self.list_of_person:
            return True
        else:
            return False
   
    def print_contents(self):
         height = 0
         amount_people = len(self.list_of_person)
         
         for person in self.list_of_person:
             height += person.height
         print(f"There are {amount_people} persons in the room, and their combined height is {height} cm")

         for person in self.list_of_person:
             print(f"{person.name} ({person.height} cm)")

         
    def shortest(self):
        shortest_person = 0
        shortest = []
        if self.is_empty():
                return None
        else:
            for person in self.list_of_person:
                if shortest_person == 0:
                    shortest_person = person.height
                    shortest.append(person)
                elif shortest_person > person.height:
                    shortest_person = person.height
                    shortest[0] = person
            return shortest[0]


    def remove_shortest(self):

        if self.is_empty():
                return None
        else:
            if self.shortest() in self.list_of_person:
                remove = self.list_of_person.index(self.shortest())
                return self.list_of_person.pop(remove)


def main():
    room = Room()
    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 140))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    
    print()

    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    print()

    room.remove_shortest()
    # print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

if __name__ == "__main__": 
    main()