# Write your solution here:

class Book:
    
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
    
    def book_input(self, name: str, author: str, genre: str, year: int):
        print(f"{author}: {name} ({year})")
        print(f"The genre of the book {name} is {genre}")
    
def main():
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    
    python.book_input(everest.author, everest.name,everest.year, everest.genre)
    python.book_input(python.author, python.name,python.year,python.genre)

if __name__ == "__main__":
    main()
