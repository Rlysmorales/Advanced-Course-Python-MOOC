# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        #The max() function returns the item with the highest value, or the item with the highest value in an iterable.
        return max(set(my_list), key = my_list.count)
    
    @classmethod
    def doubles(cls, my_list: list):
        
        counter = 0
        for duplicate in set(my_list):
            print("duplicate", duplicate)
            #The count() method returns the number of elements with the specified value.
            if my_list.count(duplicate) >= 2:
                print("my_list.count(duplicate)",my_list.count(duplicate))
                counter += 1
                print("counter",counter)
        return counter
                    

def main():
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))  
    print(ListHelper.doubles(numbers))

if __name__ == "__main__":
    main()