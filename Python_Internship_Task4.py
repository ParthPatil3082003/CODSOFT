import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors Game By Parth Patil")

        self.label_instruction = tk.Label(self.window, text="Choose Rock, Paper, or Scissors:")
        self.label_instruction.grid(row=0, column=0, columnspan=3, pady=10)

        self.button_rock = tk.Button(self.window, text="Rock", command=lambda: self.play_round("Rock"))
        self.button_rock.grid(row=1, column=0, padx=10, pady=5)

        self.button_paper = tk.Button(self.window, text="Paper", command=lambda: self.play_round("Paper"))
        self.button_paper.grid(row=1, column=1, padx=10, pady=5)

        self.button_scissors = tk.Button(self.window, text="Scissors", command=lambda: self.play_round("Scissors"))
        self.button_scissors.grid(row=1, column=2, padx=10, pady=5)

        self.label_result = tk.Label(self.window, text="Result: ")
        self.label_result.grid(row=2, column=0, columnspan=3, pady=10)

        self.label_score = tk.Label(self.window, text="Score: User - 0, Computer - 0")
        self.label_score.grid(row=3, column=0, columnspan=3, pady=10)

        self.button_play_again = tk.Button(self.window, text="Play Again", command=self.reset_game)
        self.button_play_again.grid(row=4, column=0, columnspan=3, pady=10)
        self.button_play_again.grid_remove()

    def play_round(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

        self.update_score(result)
        self.update_score_label()

        self.button_play_again.grid()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "User Wins"
        else:
            return "Computer Wins"

    def display_result(self, user_choice, computer_choice, result):
        self.label_result.config(text=f"Result: You chose {user_choice}. Computer chose {computer_choice}. {result}")

    def update_score(self, result):
        if result == "User Wins":
            self.user_score += 1
        elif result == "Computer Wins":
            self.computer_score += 1

    def update_score_label(self):
        self.label_score.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def reset_game(self):
        self.label_result.config(text="Result: ")
        self.button_play_again.grid_remove()


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.window.mainloop()
