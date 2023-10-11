class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address = address


class PhoneBook(Person):
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
     
        if not name in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):

        if not name in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_address(address)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()

    def get_address(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()

    def all_entries(self):
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def user_choice(self):
        print("Commands: ")
        print("0 Exit")
        print("1 Add Number")
        print("2 Search")
        print("3 Add Address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        address = self.__phonebook.get_address(name)
        if numbers == None or numbers == []:
            print("number unknown")
        else:
            for number in numbers:
                print(number)
        if address == None:
            print("address unknown")
        else:
            print(address)

    def execute(self):
        self.user_choice()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.user_choice()


def main():
    # when testing, no code should be outside application except the following:
    application = PhoneBookApplication()
    application.execute()

    # person = Person("Eric")
    # print(person.name())
    # print(person.numbers())
    # print(person.address())
    # person.add_number("040-123456")
    # person.add_address("Mannerheimintie 10 Helsinki")
    # print(person.numbers())
    # print(person.address())


    # phonebook = PhoneBook()
    # phonebook.add_number("Eric", "02-123456")
    # print(phonebook.get_entry("Eric"))
    # print(phonebook.get_entry("Emily"))

if __name__ == "__main__":
    main()