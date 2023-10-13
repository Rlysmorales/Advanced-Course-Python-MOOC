# Write your solution here:
import random
def word_generator(characters: str, length: int, amount: int):
    count = 0
    new_string = ""
    while count < amount:
        word = ([random.choice(characters) for i in range(length)])
        yield new_string.join(word)
        count +=1


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    
    for word in wordgen:
        print(word)
