import pygame
import random

choices = ["Rock", "Paper", "Scissors"]
class RPS:
    def __init__(self,player_choice, computer_choice, count):
        self.player_choice = player_choice
        self.computer_choice = "None"
        #self.result = "None"
        self.count = count

    def play(self, player_choice):
        print('Hi')
        self.player_choice = player_choice
        self.computer_choice = random.choice(choices)
        print(player_choice)
        print(self.computer_choice)
        if self.player_choice == self.computer_choice:
            print ("Tied")
            pass
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
                (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
                (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            print ('You win!!!')
            
        else:
            print ("Com wins")
            


