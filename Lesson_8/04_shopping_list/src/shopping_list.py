# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------
def total_units(my_list: ShoppingList):
        number_items = []
        for total_items in range(1, my_list.number_of_items()+1):
            number_items.append(my_list.amount(total_items))
            adding_list = (sum(number_items))
        return adding_list


def main():
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))
    
if __name__ == "__main__":
    main()