# Write your solution here
def main():

    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)

def row_sums(my_matrix: list):

    for number in my_matrix:
        number.append(sum(number))
        print(my_matrix)

if __name__ == "__main__":
    main()
