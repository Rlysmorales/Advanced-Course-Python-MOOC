# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
       
        if len(player1_word) > len(player2_word):

            return 1
            
        elif len(player2_word) > len(player1_word):

            return 2
        else:
            pass

class MostVowels(WordGame): 

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        player_one_count = 0
        player_two_count = 0
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        for word in player1_word:
            if word in vowels:
                player_one_count += 1

        for word2 in player2_word:
            if word2 in vowels:
                player_two_count += 1
       
        if player_two_count > player_one_count:

            return 2
        elif player_two_count < player_one_count:

            return 1
    
        else:
            pass
             

class RockPaperScissors(WordGame): 

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here

        words = ["rock", "scissors", "paper"]
        if player1_word == player2_word:

            pass
        
        elif player1_word not in words and player2_word not in words:

            pass
        
        elif player1_word in words and player2_word not in words:

            return 1
        
        elif player1_word not in words and player2_word in words:

            return 2

        elif player1_word == "rock" and player2_word == "paper":

            return 2

        elif player1_word == "paper" and player2_word == "rock":

            return 1

        elif player1_word == "rock" and player2_word == "scissors":

            return 1

        elif player1_word == "scissors" and player2_word == "rock":

            return 2

        elif player1_word == "paper" and player2_word == "scissors":

            return 2

        elif player1_word == "scissors" and player2_word == "paper":

            return 1
        else:
            pass


def main():

    p = LongestWord(3)
    p.play()

    vowels = MostVowels(3)
    vowels.play()

    rock = RockPaperScissors(4)
    rock.play()    


if __name__ == "__main__":
    main()
