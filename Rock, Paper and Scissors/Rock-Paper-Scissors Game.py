import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.scores = {'user': 0, 'computer': 0}

    def get_user_choice(self):
        user_choice = input("Choose rock, paper, or scissors: ")
        while user_choice not in self.choices:
            print("Invalid choice. Please try again.")
            user_choice = input("Choose rock, paper, or scissors: ")
        return user_choice

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
           (user_choice == 'paper' and computer_choice == 'rock') or \
           (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'user'
        return 'computer'

    def display_result(self, user_choice, computer_choice, winner):
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
        else:
            print("Computer wins!")

    def update_scores(self, winner):
        if winner != 'tie':
            self.scores[winner] += 1

    def play_again(self):
        play_again = input("Do you want to play another round? (yes/no): ")
        return play_again.lower() == 'yes'

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, winner)
            self.update_scores(winner)
            print(f"Scores: User - {self.scores['user']}, Computer - {self.scores['computer']}")
            if not self.play_again():
                break

game = RockPaperScissors()
game.play()
