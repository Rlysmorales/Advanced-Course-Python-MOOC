# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError('The length must not be below zero')

    @property
    def length(self):

         return self.__length 

    @length.setter
    def length(self, length: int):
        try: 
            if length >0:
                self.__length = length
        except ValueError:
                print("The length must not be below zero")


def main():
    the_wall = Recording(-1)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)

if __name__ == "__main__":
    main()